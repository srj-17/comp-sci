import Tree from "./balanced-bst.js";

function randomArray(size) {
    let arr = [];
    for (let i = 0; i < size; i++) {
        arr = arr.concat(Math.floor(Math.random() * 100));
    }
    return arr;
}

console.log("Random tree: ");
const tree = new Tree(randomArray(5));
tree.prettyPrint();

console.log(`Is it balanced? ${tree.isBalanced() ? "yes" : "no"}`);
console.log("\nPre Order traversal: ");
tree.preOrder((data) => {
    console.log(data);
});

console.log("\npost Order traversal: ");
tree.postOrder((data) => {
    console.log(data);
});

console.log("\nin Order traversal: ");
tree.inOrder((data) => {
    console.log(data);
});

console.log("\nUnbalancing the tree by adding 150, 170, 190");
tree.insert(150);
tree.insert(170);
tree.insert(190);
tree.prettyPrint();
console.log(`Is it balanced now? ${tree.isBalanced() ? "yes" : "no"}`);

console.log("\nBalancing the tree again.");
tree.reBalance();
tree.prettyPrint();
console.log(`Is it balanced now? ${tree.isBalanced() ? "yes" : "no"}`);

console.log("\nPre Order traversal: ");
tree.preOrder((data) => {
    console.log(data);
});

console.log("\npost Order traversal: ");
tree.postOrder((data) => {
    console.log(data);
});

console.log("\nin Order traversal: ");
tree.inOrder((data) => {
    console.log(data);
});
