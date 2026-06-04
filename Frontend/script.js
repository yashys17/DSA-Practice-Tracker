let allProblems = [];

// Load Stats
fetch("/stats")
.then(response => response.json())
.then(data => {

    document.getElementById("total").innerText = data.total_problems;
    document.getElementById("easy").innerText = data.easy;
    document.getElementById("medium").innerText = data.medium;
    document.getElementById("hard").innerText = data.hard;

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

// Load Problems
fetch("/problems")
.then(response => response.json())
.then(data => {

    allProblems = data;

    renderProblems(data);

});

// Render Problems
function renderProblems(data){

    let table = document.getElementById("problemTable");

    table.innerHTML = "";

    data.forEach(problem => {

        let difficultyClass = "hard";

        if(problem.difficulty === "Easy"){
            difficultyClass = "easy";
        }
        else if(problem.difficulty === "Medium"){
            difficultyClass = "medium";
        }

        let linkHTML = "-";

        if(problem.problem_link){
            linkHTML = `
            <a
            href="${problem.problem_link}"
            target="_blank"
            onclick="markPending(${problem.id})">
            Open
            </a>
            `;
        }

        let statusHTML = "";

        if(problem.status === "Solved"){

            statusHTML = `
            <span style="color:green;font-weight:bold;">
                🟢 Solved
            </span>
            `;

        }
        else if(problem.status === "Pending"){

            statusHTML = `
            <span style="color:orange;font-weight:bold;">
                🟡 Pending
            </span>
            <br><br>
            <button onclick="markSolved(${problem.id})">
                Mark Solved
            </button>
            `;

        }
        else{

            statusHTML = `
            <span style="color:red;font-weight:bold;">
                🔴 Unsolved
            </span>
            <br><br>
            <button onclick="markSolved(${problem.id})">
                Mark Solved
            </button>
            `;

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

            <td>
                ${statusHTML}
            </td>

            <td>
                ${linkHTML}
            </td>

            <td>
                <button onclick='showNotes(${JSON.stringify(problem.notes || "No Notes")})'>
                    View
                </button>
            </td>

            <td>
                ${
                    problem.status === "Solved"
                    ? (problem.date_solved || "-")
                    : "-"
                }
            </td>

        </tr>
        `;
    });

}

// Search Problems
function searchProblem(){

    let value =
    document.getElementById("searchBox")
    .value
    .toLowerCase();

    let filtered =
    allProblems.filter(problem =>

        problem.title.toLowerCase().includes(value) ||

        problem.topic.toLowerCase().includes(value)

    );

    renderProblems(filtered);

}

// Filter Problems
function filterProblems(){

    let difficulty =
    document.getElementById("difficultyFilter").value;

    let platform =
    document.getElementById("platformFilter").value;

    let filtered =
    allProblems.filter(problem => {

        let difficultyMatch =
        difficulty === "All" ||
        problem.difficulty === difficulty;

        let platformMatch =
        platform === "All" ||
        problem.platform === platform;

        return difficultyMatch && platformMatch;

    });

    renderProblems(filtered);

}

// Notes Modal
function showNotes(notes){

    document.getElementById("noteText").innerText = notes;

    document.getElementById("notesModal").style.display = "block";

}

function closeNotes(){

    document.getElementById("notesModal").style.display = "none";

}

// Mark Pending
function markPending(problemId){

    fetch(
        `/pending/${problemId}`,
        {
            method: "PUT"
        }
    );

}

// Mark Solved
function markSolved(problemId){

    fetch(
        `/solve/${problemId}`,
        {
            method: "PUT"
        }
    )
    .then(response => response.json())
    .then(data => {

        alert("Problem Marked Solved");

        location.reload();

    });

}

// Dark Mode
document
.getElementById("themeBtn")
.addEventListener("click", () => {

    document.body.classList.toggle("dark");

});

// Streak
fetch("/streak")
.then(response => response.json())
.then(data => {

    document.getElementById("streak").innerText =
    data.streak + " Days";

});

// Progress
fetch("/progress")
.then(response => response.json())
.then(data => {

    document.getElementById("progress").innerText =
    data.percent + "%";

});

// Topic Analytics
fetch("/topics")
.then(response => response.json())
.then(data => {

    let labels = [];
    let values = [];

    data.forEach(item => {

        labels.push(item[0]);
        values.push(item[1]);

    });

    new Chart(
        document.getElementById("topicChart"),
        {
            type: "pie",
            data: {
                labels: labels,
                datasets: [{
                    data: values
                }]
            }
        }
    );

});

// Export Report
function exportReport(){

    fetch("/export")
    .then(response => response.json())
    .then(data => {

        alert("Report Exported Successfully");

    });

}