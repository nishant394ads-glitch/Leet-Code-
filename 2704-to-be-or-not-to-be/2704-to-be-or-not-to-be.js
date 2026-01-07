/**
 * @param {any} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: function(other) {
            if (val === other) return true;
            throw new Error("Not Equal");
        },
        notToBe: function(other) {
            if (val !== other) return true;
            throw new Error("Equal");
        }
    };
};
