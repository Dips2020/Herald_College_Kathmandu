
function higher_order() {
    const items = [1, 29, 47]
    const copy = [];
    items.forEach(function (item) {
        copy.push(item * item);
    });
    return copy
    // return { ...copy, items };
}
console.log(higher_order())