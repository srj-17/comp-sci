import mergeSort from "../../recursion/merge-sort.js";

function Node(data) {
    let left = null;
    let right = null;
    return { data, left, right };
}

class Tree {
    constructor(arr) {
        this.root = this.buildTree(arr);
    }

    buildTree(arr) {
        if (arr.length <= 0) return null;

        arr = this.#sortAndRemoveDuplicates(arr);

        // in case array.length is odd
        let mid = Math.floor(arr.length / 2);
        const root = Node(arr[mid]);

        // arr.slice isn't inclusive of the last index
        root.left = this.buildTree(arr.slice(0, mid));
        root.right = this.buildTree(arr.slice(mid + 1, arr.length));

        return root;
    }

    #sortAndRemoveDuplicates(arr) {
        const uniqueArray = [...new Set(arr)];
        const mergedArray = mergeSort(uniqueArray);
        return mergedArray;
    }

    // we don't need to check the left subtree cause
    // for inorder traversal, we go from left->root->right,
    // and we're given the root
    #inOrderSuccessor(node) {
        let curr = node.right;

        // since we want to find the inorder successor which
        // should be of the least value greater than the current
        // node's value,
        // and left nodes contain values less than the current value
        // we loop till we can no longer find the left nodes
        while (curr !== null && curr.left !== null) {
            curr = curr.left;
        }

        return curr;
    }

    insert(data, node = this.getTree()) {
        if (node === null) return Node(data);

        if (node.data === data) return node;

        if (data <= node.data) node.left = this.insert(data, node.left);
        else node.right = this.insert(data, node.right);

        return node;
    }

    remove(data, node = this.getTree()) {
        // base case
        if (node === null) return node;

        // these 2 cases deal with finding the data
        if (data < node.data) node.left = this.remove(data, node.left);
        else if (data > node.data) node.right = this.remove(data, node.right);
        // this case deals with when data is found, removing the data
        // if data = node.data
        else {
            // if it has right node, but no left
            if (!node.left) return node.right;

            if (!node.right) return node.left;

            // if it has no children, meaning node.left and node.right are null,
            // the above conditions handle that case

            // if it has both children, replace it with the inOrderSuccessor of the node

            // i.e. put inorder successor in place of current node
            let successor = this.#inOrderSuccessor(node);
            node.data = successor.data;

            // and remove the inorder successor
            this.remove(successor.data, node.right);
        }

        // return the node as is if the data is not found
        return node;
    }

    getTree() {
        return this.root;
    }

    find(data, root = this.getTree()) {
        if (root === null) return null;

        if (data === root.data) return root;

        if (data < root.data) return this.find(data, root.left);

        if (data > root.data) return this.find(data, root.right);
    }

    // NOTE: I'm not using queue, I'm just simulating it with
    // unshift and pop FIFO
    // TODO: Do this in recursive manner
    levelOrder(callback, root = this.getTree()) {
        if (typeof callback !== "function")
            throw new TypeError("Argument of type function Expected");

        let first = [];
        first.unshift(root);
        while (first.length !== 0) {
            // dequeue the first node
            const node = first.pop();

            if (node !== null) {
                // process the first node
                const data = node.data;
                callback(data);

                // queue the children of the node in order
                first.unshift(node.left);
                first.unshift(node.right);
            }
        }
    }

    inOrder(callback, root = this.getTree()) {
        if (typeof callback !== "function")
            throw new TypeError("Argument of type function Expected");

        if (root === null) return;

        this.inOrder(callback, root.left);
        callback(root.data);
        this.inOrder(callback, root.right);
    }

    preOrder(callback, root = this.getTree()) {
        if (typeof callback !== "function")
            throw new TypeError("Argument of type function Expected");

        if (root === null) return;

        callback(root.data);
        this.preOrder(callback, root.left);
        this.preOrder(callback, root.right);
    }

    postOrder(callback, root = this.getTree()) {
        if (typeof callback !== "function")
            throw new TypeError("Argument of type function Expected");

        if (root === null) return;

        this.postOrder(callback, root.left);
        this.postOrder(callback, root.right);
        callback(root.data);
    }

    height(node = this.getTree()) {
        // we get height + 1 when we reach null and we and -1 to that to
        // get the actual height
        if (node === null) return -1;

        // in case the node has both children
        if (this.height(node.left) > this.height(node.right)) {
            return 1 + this.height(node.left);
        } else {
            return 1 + this.height(node.right);
        }
    }

    depth(node, root = this.getTree()) {
        if (node === root) return 0;
        if (node === null)
            throw new TypeError("Node of type node expected. Got null!");
        if (node.data > root.data) return 1 + this.depth(node, root.right);
        if (node.data < root.data) return 1 + this.depth(node, root.left);
    }

    isBalanced(root = this.getTree()) {
        if (!root) return true;
        let leftHeight = this.height(root.left);
        let rightHeight = this.height(root.right);

        return (
            Math.abs(leftHeight - rightHeight) <= 1 &&
            this.isBalanced(root.left) &&
            this.isBalanced(root.right)
        );
    }

    reBalance() {
        let arr = [];
        this.inOrder((data) => {
            arr = arr.concat(data);
        });
        this.root = this.buildTree(arr);
    }

    // to prettyPrint the tree
    prettyPrint(node = this.root, prefix = "", isLeft = true) {
        if (node === null) {
            return;
        }
        if (node.right !== null) {
            this.prettyPrint(
                node.right,
                `${prefix}${isLeft ? "│   " : "    "}`,
                false,
            );
        }
        console.log(`${prefix}${isLeft ? "└── " : "┌── "}${node.data}`);
        if (node.left !== null) {
            this.prettyPrint(
                node.left,
                `${prefix}${isLeft ? "    " : "│   "}`,
                true,
            );
        }
    }
}

export default Tree;
