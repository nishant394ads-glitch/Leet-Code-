var cancellable = function(fn, args, t) {
    fn(...args); // run immediately
    
    const intervalId = setInterval(() => {
        fn(...args);
    }, t);
    
    return function cancelFn() {
        clearInterval(intervalId);
    };
};
