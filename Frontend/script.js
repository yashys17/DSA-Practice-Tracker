

// Load Statistics

fetch("http://127.0.0.1:5000/stats")
.then(response => response.json())
.then(data => {

    document.getElementById("total").innerText =
    data.total_problems;

    document.getElementById("easy").innerText =
    data.easy;

    document.getElementById("medium").innerText =
    data.medium;

    document.getElementById("hard").innerText =
    data.hard;

    new Chart(
        document.getElementById("myChart"),
        {
            type: "bar",
            data: {
                labels: ["Easy", "Medium", "Hard"],
                datasets: [{
                    label: "Problems Solved",
                    data: [
                        data.easy,
                        data.medium,
                        data.hard
                    ]
                }]
            },
            options: {
                responsive: true
            }
        }
    );

});



// Load Problems Table

fetch("http://127.0.0.1:5000/problems")
.then(response => response.json())
.then(data => {

    let table =
    document.getElementById("problemTable");

    data.forEach(problem => {

        let difficultyClass = "";

        if(problem.difficulty === "Easy"){
            difficultyClass = "easy";
        }
        else if(problem.difficulty === "Medium"){
            difficultyClass = "medium";
        }
        else{
            difficultyClass = "hard";
        }

        table.innerHTML += `
        <tr>
            <td>${problem.id}</td>
            <td>${problem.title}</td>
            <td>${problem.topic}</td>

            <td>
                <span class="${difficultyClass}">
                    ${problem.difficulty}
                </span>
            </td>

            <td>
                <span class="platform">
                    ${problem.platform}
                </span>
            </td>
        </tr>
        `;

    });

});



// Add New Problem

function addProblem(){

    let title =
    document.getElementById("title").value;

    let topic =
    document.getElementById("topic").value;

    let difficulty =
    document.getElementById("difficulty").value;

    let platform =
    document.getElementById("platform").value;

    if(title === "" || topic === ""){
        alert("Please fill all fields");
        return;
    }

    fetch(
        "http://127.0.0.1:5000/add-problem",
        {
            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                title:title,
                topic:topic,
                difficulty:difficulty,
                platform:platform
            })
        }
    )
    .then(response => response.json())
    .then(data => {

        alert("Problem Added Successfully");

        location.reload();

    });

}



// Search Problems

function searchProblem(){

    let value =
    document.getElementById("searchBox")
    .value
    .toLowerCase();

    let rows =
    document.querySelectorAll("#problemTable tr");

    rows.forEach(row => {

        if(
            row.innerText
            .toLowerCase()
            .includes(value)
        ){
            row.style.display = "";
        }
        else{
            row.style.display = "none";
        }

    });

}



// Dark Mode

document
.getElementById("themeBtn")
.addEventListener("click", () => {

    document.body.classList.toggle("dark");

});
