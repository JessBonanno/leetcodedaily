var myFunc = function(myStr) {
    console.log(myStr);
    return myStr;
  }
console.log(setTimeout(function(timeoutArgument) {
    myFunc('Hello World')
  }, 1500))
