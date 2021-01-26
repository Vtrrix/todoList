//the div that contains all the todos
let list = document.getElementById("todos");

//to store all todos
let todoList = [];

//To print all todos . Its like a refresh for todo list
let showTodos = () => {
	let i = 0;
	list.innerHTML = ` `;
	// for(var i=0 ; i < todoList.length-1 ; i++)
	todoList.map((ele) => {
		list.innerHTML += `
            <div class="task">
                <input type="checkbox" class="checkBox" onclick="checkIt(${i})">
                <div class="taskText">
                    ${ele.title}
                </div>
                <button class="delete" onclick="deleteTodo(${i})">
                    <img src="./img/bin.png" alt="delete">
                </button>
            </div>
            <hr class="line">

        `;
		i++;
	});

	let checks = document.querySelectorAll(".checkBox");

	for (i = 0; i < checks.length; i++) {
		todoList[i].status
			? (document.getElementsByClassName("checkBox")[i].checked = false)
			: (document.getElementsByClassName("checkBox")[i].checked = true);
		checkIt(i);
	}
};

//To add a new todo to the list
function addNew() {
	let todo = document.getElementById("newTodo").value;

	if (todo) {
		let newTodo = {
			title: todo,
			status: true,
		};
		todoList.unshift(newTodo);
	} else {
		alert("Please Input some data!");
	}

	//Should I do it this way ???
	// todo ? ()=> {

	//     newTodo={
	//             title:todo,
	//             status:true
	//         }
	//     todoList.unshift(newTodo);

	// }
	// : ()=>{
	//     alert("Please Input some data!");
	// }

	showTodos();
	document.getElementById("newTodo").value = null;
}

//To delete a todo

let deleteTodo = (index) => {
	if (confirm("Are You Sure ?")) {
		todoList.splice(index, 1);
		showTodos();
	}
};

//To check and uncheck checkbox next to task

let checkIt = (index) => {
	let cBox = document.getElementsByClassName("checkBox")[index];

	if (cBox.checked) {
		todoList[index].status = false;
		document.getElementsByClassName("taskText")[index].style.textDecoration =
			"line-through 2px solid rgb(34, 34, 34)";
	} else {
		todoList[index].status = true;
		document.getElementsByClassName("taskText")[index].style.textDecoration =
			"none";
	}
};

document.getElementById("newTodo").addEventListener("keydown", (e) => {
	if (e.keyCode === 13) {
		addNew();
	}
});
