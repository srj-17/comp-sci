import LinkedList from "../linked-list/linked-list.js";
import { Node } from "../linked-list/linked-list.js";

function HashMap() {
    const loadFactor = 0.75;
    // we can't do buckets.length, because that just keeps changing in js
    let capacity = 16;
    let entryCount = 0;
    const buckets = [];

    function updateBucket() {
        return entryCount > loadFactor * capacity;
    }

    const length = () => entryCount;

    const getCapacity = () => capacity;

    const getLoadLevel = () => entryCount / capacity;

    function has(key) {
        const index = hash(key);

        try {
            if (index < 0 || index >= buckets.length) {
                throw new Error("Trying to access index out of bounds");
            }
            const linkedListHead = buckets[index].head;

            let temp = linkedListHead;
            while (temp !== null) {
                if (temp.value.key === key) {
                    return true;
                }

                temp = temp.next;
            }

            return false;
        } catch (e) {
            console.error(e.message);
            return false;
        }
    }

    function update(key, value) {
        const index = hash(key);
        const linkedListHead = buckets[index].head;

        let temp = linkedListHead;
        while (temp !== null) {
            if (temp.value.key === key) {
                temp.value.value = value;
                return;
            }

            temp = temp.next;
        }
    }

    // we don't need to copy the array to a new array because
    // in javaScript, array can grow, so we can just increase its capacity
    function updateCapacity() {
        capacity = capacity * 2;
    }

    function hash(key) {
        let hashCode = 0;

        const primeNumber = 31;
        for (let i = 0; i < key.length; i++) {
            hashCode = primeNumber * hashCode + key.charCodeAt(i);
            // so that the hashCode never becomes larger number than what our
            // javaScript can handle
            hashCode = hashCode % capacity;
        }

        return hashCode;
    }

    function set(key, value) {
        const index = hash(key);

        // prevent javaScript's dynamic array length for buckets
        // for the purposes of hash map learning
        if (index < 0 || index >= capacity) {
            throw new Error("Trying to access index out of bounds");
        }

        // if nothing in the index, put the value directly
        if (!buckets[index]) {
            buckets[index] = new LinkedList();
        }

        // check if the key already exists
        if (has(key)) {
            update(key, value);
        } else {
            buckets[index].append({ key, value });
            // increase number of entires if we append one
            entryCount++;
        }

        if (updateBucket()) {
            updateCapacity();
        }
    }

    function get(key) {
        const index = hash(key);

        try {
            // if trying to access out of bounds key, ofc, return null right away
            if (index < 0 || index >= buckets.length) {
                throw new Error("Trying to access index out of bounds");
            }

            // get the linked list for the index and traverse through it
            // to get the value
            let temp = buckets[index].head;
            while (temp !== null) {
                if (temp.value.key === key) {
                    return temp.value.value;
                }

                temp = temp.next;
            }

            return null;
        } catch (e) {
            console.error(e.message);
            return null;
        }
    }

    function remove(key) {
        if (!has(key)) {
            return false;
        }

        const index = hash(key);
        let linkedListHead = buckets[index].head;

        // if value in the head
        if (linkedListHead.value.key === key) {
            buckets[index].head = linkedListHead.next;

            entryCount--;
            return true;
        }

        // get the node that contains the key within the bucket
        // and remove it
        let temp = linkedListHead;

        while (temp.next !== null) {
            if (temp.next.value.key === key) {
                temp.next = temp.next.next;
                entryCount--;
                return true;
            }
            temp = temp.next;
        }

        return false;
    }

    function clear() {
        buckets.forEach((bucket) => {
            bucket = null;
        });
        entryCount = 0;
    }

    function keys() {
        let keys = [];
        buckets.forEach((bucket) => {
            if (bucket === null) return;
            const linkedListHead = bucket.head;
            let temp = linkedListHead;
            while (temp !== null) {
                keys = keys.concat(temp.value.key);
                temp = temp.next;
            }
        });

        return keys;
    }

    function values() {
        let values = [];
        buckets.forEach((bucket) => {
            if (bucket === null) return;
            const linkedListHead = bucket.head;
            let temp = linkedListHead;
            while (temp !== null) {
                values = values.concat(temp.value.value);
                temp = temp.next;
            }
        });

        return values;
    }

    function values() {
        let values = [];
        buckets.forEach((bucket) => {
            if (bucket === null) return;
            const linkedListHead = bucket.head;
            let temp = linkedListHead;
            while (temp !== null) {
                values = values.concat(temp.value.value);
                temp = temp.next;
            }
        });

        return values;
    }

    function entries() {
        let entries = [];
        buckets.forEach((bucket) => {
            if (bucket === null) return;
            const linkedListHead = bucket.head;
            let temp = linkedListHead;
            while (temp !== null) {
                entries = entries.concat({
                    [temp.value.key]: temp.value.value,
                });
                temp = temp.next;
            }
        });

        return entries;
    }

    return {
        set,
        get,
        has,
        remove,
        length,
        clear,
        keys,
        values,
        entries,
        getCapacity,
        getLoadLevel,
    };
}

// odin test
const test = HashMap();

// populating the map
test.set("apple", "red");
test.set("banana", "yellow");
test.set("carrot", "orange");
test.set("dog", "brown");
test.set("elephant", "gray");
test.set("frog", "green");
test.set("grape", "purple");
test.set("hat", "black");
test.set("ice cream", "white");
test.set("jacket", "blue");
test.set("kite", "pink");
test.set("lion", "golden");
console.log(test.length());

// updating the values
console.log("Below load levels (on the border 0.75)");
test.set("lion", "yellow");
console.log(`Entries count: ${test.length()}`);
console.log(`Capacity: ${test.getCapacity()}`);
console.log(`Load Level: ${test.getLoadLevel()}`);

// testing setting over load limit
console.log("\nAfter adding additional element to hash map");
test.set("moon", "silver");
console.log(`Entries count: ${test.length()}`);
console.log(`Capacity: ${test.getCapacity()}`);
console.log(`Load Level: ${test.getLoadLevel()}`);

// additional test
console.log("\nAdditional test: ");
test.set("Rama", "hello");
test.set("Rama", "hellB");
test.set("Sita", "hello");
test.set("gita", "hello");
test.set("Rita", "hari");
console.log(test.get("Rama"));
console.log(test.get("Ram"));
console.log(test.has("Rama"));
console.log(test.has("Ram"));
console.log(test.remove("Rama"));
console.log(test.remove("gita"));
console.log(test.length());
console.log(test.keys());
console.log(test.values());
console.log(test.entries());
