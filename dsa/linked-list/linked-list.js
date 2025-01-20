function Node() {
    return {
        value: null,
        next: null,
    };
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    append(value) {
        if (this.head === null) {
            this.head = Node();
            this.head.value = value;
            return;
        }

        let temp = this.head;
        while (temp.next != null) {
            temp = temp.next;
        }

        temp.next = Node();
        temp.next.value = value;
    }

    prepend(value) {
        let temp = Node();
        temp.value = value;
        temp.next = this.head;
        this.head = temp;
    }

    size() {
        let count = 0;
        let temp = this.head;
        while (temp != null) {
            count++;
            temp = temp.next;
        }
        return count;
    }

    getHead() {
        return this.head;
    }

    tail() {
        let temp = this.head;
        while (temp.next != null) {
            temp = temp.next;
        }

        return temp;
    }

    // 0 indexing
    at(index) {
        let temp = this.head;
        for (let i = 0; i < index; i++) {
            temp = temp.next;
        }

        return temp;
    }

    pop() {
        let temp = this.head;
        // travel till second last node
        while (temp.next.next != null) {
            temp = temp.next;
        }

        const poppedNode = temp.next;

        // pop the node
        temp.next = null;
        return poppedNode;
    }

    contains(value) {
        let temp = this.head;
        while (temp != null) {
            if (temp.value === value) return true;
            temp = temp.next;
        }
        return false;
    }

    find(value) {
        let temp = this.head;
        let index = 0;
        while (temp != null) {
            if (temp.value === value) return index;
            index++;
            temp = temp.next;
        }
    }

    toString() {
        let temp = this.head;
        let string = ``;
        while (temp != null) {
            string = string.concat(`(${temp.value}) -> `);
            temp = temp.next;
        }
        string = string.concat(`null`);
        return string;
    }

    insertAt(index, value) {
        if (index >= this.size()) return false;

        if (index === 0) {
            this.prepend(value);
            return true;
        }

        if (index === this.size() - 1) {
            this.append(value);
            return true;
        }

        // get to the index
        let temp = this.head;
        for (let i = 0; i < index - 1; i++) {
            temp = temp.next;
        }

        // create the node
        let node = Node();
        node.value = value;

        // insert the node
        node.next = temp.next;
        temp.next = node;
        return true;
    }

    removeAt(index) {
        if (index >= this.size()) return false;

        if (index === 0) {
            this.head = this.head.next;
            return;
        }

        if (index === this.size() - 1) {
            this.pop();
            return;
        }

        // get to the index
        let temp = this.head;
        for (let i = 0; i < index - 1; i++) {
            temp = temp.next;
        }

        // remove the node
        temp.next = temp.next.next;
        temp.next.next = null;
        return true;
    }
}

const ll = new LinkedList();
ll.append(2);
ll.prepend(1);
ll.append(5);
ll.append(8);

console.log("");
console.log("Self test: ");
console.log("------------------------------------");
console.log(`Size: ${ll.size()}`);
console.log(`String: ${ll.toString()}`);
console.log(`Tail: ${ll.tail().value}`);
console.log(`Head: ${ll.getHead().value}`);
console.log(`At 1 (0 indexed): ${ll.at(1).value}`);
console.log(`Pop: ${ll.pop().value}`);
console.log(`String after pop: ${ll.toString()}`);
console.log(`Contains 2: ${ll.contains(2)}`);
console.log(`Contains 5: ${ll.contains(5)}`);
console.log(`Index of 2 (0 indexed): ${ll.find(2)}`);
// first index
ll.insertAt(1, 9);
// middle index
ll.insertAt(0, 10);
// last index
ll.insertAt(4, 3);
console.log(`String after insertAt: ${ll.toString()}`);
// first index
ll.removeAt(0);
// middle index
ll.removeAt(3);
// last index
ll.removeAt(3);
console.log(`String after removeAt: ${ll.toString()}`);

export default LinkedList;
