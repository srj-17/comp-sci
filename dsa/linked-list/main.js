import LinkedList from "./linked-list.js";

console.log("");
console.log("Test for the project: ");
console.log("------------------------------");
// example uses class syntax - adjust as necessary
const list = new LinkedList();

list.append("dog");
list.append("cat");
list.append("parrot");
list.append("hamster");
list.append("snake");
list.append("turtle");
console.log(list.toString());
