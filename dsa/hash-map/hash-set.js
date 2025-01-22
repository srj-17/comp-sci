import LinkedList from "../linked-list/linked-list.js";

function HashSet() {
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

            if (!buckets[index]) return false;

            const linkedListHead = buckets[index].head;

            let temp = linkedListHead;
            while (temp !== null) {
                if (temp.value === key) {
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

    function set(key) {
        const index = hash(key);

        // prevent javaScript's dynamic array length for buckets
        // for the purposes of hash set learning
        if (index < 0 || index >= capacity) {
            throw new Error("Trying to access index out of bounds");
        }

        // if nothing in the index, put the value directly
        if (!buckets[index]) {
            buckets[index] = new LinkedList();
        }

        // check if the key already exists
        if (has(key)) {
            return;
        } else {
            buckets[index].append(key);
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
            if (!buckets[index]) {
                return null;
            }

            let temp = buckets[index].head;

            while (temp !== null) {
                if (temp.value === key) {
                    return temp.value;
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
        if (linkedListHead.value === key) {
            buckets[index].head = linkedListHead.next;

            entryCount--;
            return true;
        }

        // get the node that contains the key within the bucket
        // and remove it
        let temp = linkedListHead;

        while (temp.next !== null) {
            if (temp.next.value === key) {
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
                keys = keys.concat(temp.value);
                temp = temp.next;
            }
        });

        return keys;
    }

    function entries() {
        let entries = [];
        buckets.forEach((bucket) => {
            if (bucket === null) return;
            const linkedListHead = bucket.head;
            let temp = linkedListHead;
            while (temp !== null) {
                entries = entries.concat(temp.value);
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
        entries,
        getCapacity,
        getLoadLevel,
    };
}

// odin test
const test = HashSet();

// populating the set
test.set("apple");
test.set("banana");
test.set("carrot");
test.set("dog");
test.set("elephant");
test.set("frog");
test.set("grape");
test.set("hat");
test.set("ice cream");
test.set("jacket");
test.set("kite");
test.set("lion");
console.log(test.length());

// updating the values
console.log("Below load levels (on the border 0.75)");
test.set("lion");
console.log(`Entries count: ${test.length()}`);
console.log(`Capacity: ${test.getCapacity()}`);
console.log(`Load Level: ${test.getLoadLevel()}`);

// testing setting over load limit
console.log("\nAfter adding additional element to hash set");
test.set("moon", "silver");
console.log(`Entries count: ${test.length()}`);
console.log(`Capacity: ${test.getCapacity()}`);
console.log(`Load Level: ${test.getLoadLevel()}`);

//// additional test
console.log("\nAdditional test: \n");
test.set("Rama");
test.set("Rama");
test.set("Sita");
test.set("gita");
test.set("Rita");
console.log(`Get Rama: ${test.get("Rama")}`);
console.log(`Get Ram: ${test.get("Ram")}`);
console.log(`Has rama: ${test.has("Rama")}`);
console.log(`Has ram: ${test.has("Ram")}`);
console.log(`Remove Rama: ${test.remove("Rama")}`);
console.log(`Remove Gita: ${test.remove("gita")}`);
console.log(`Length: ${test.length()}`);
console.log(`Keys: ${test.keys()}`);
console.log(`Entries: ${test.entries()}`);
