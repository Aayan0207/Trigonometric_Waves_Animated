document.addEventListener("DOMContentLoaded", function () {
  const trigs = document.querySelectorAll(".square");
  const turtleCode = document.querySelector("#turtlecode");
  trigs.forEach((trig) => {
    trig.addEventListener("click", function () {
      if (trig.value) {
        trig.value = "";
        trig.style.border = "4px solid black";
      } else {
        trig.value = this.placeholder;
        trig.style.border = "4px solid turquoise";
      }
    });
  });
  const trigForm = document.querySelector("#Trig-form");
  trigForm.onsubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(trigForm);
    fetch("/", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        turtleCode.value = data.python_code;
        runit();
      })
      .catch((error) => {
        console.log(error);
      });
  };
});

function outf(text) {
  var mypre = document.getElementById("output");
  mypre.innerHTML = mypre.innerHTML + text;
}

function builtinRead(x) {
  if (
    Sk.builtinFiles === undefined ||
    Sk.builtinFiles["files"][x] === undefined
  )
    throw "File not found: '" + x + "'";
  return Sk.builtinFiles["files"][x];
}

function runit() {
  var prog = document.getElementById("turtlecode").value;
  var mypre = document.getElementById("output");
  mypre.innerHTML = "";
  Sk.pre = "output";
  Sk.configure({ output: outf, read: builtinRead });
  (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = "mycanvas";
  Sk.TurtleGraphics.width = "520";
  Sk.TurtleGraphics.height = "500";
  var myPromise = Sk.misceval.asyncToPromise(function () {
    return Sk.importMainWithBody("<stdin>", false, prog, true);
  });
  myPromise.then(
    function (mod) {
      console.log("success");
    },
    function (err) {
      console.log(err.toString());
    }
  );
}
