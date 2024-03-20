

// exams = [
//     {
//         "exam_id": 1,
//         "exam_date": "2024-01-15",
//         "start_time": "09:00:00",
//         "end_time": "12:00:00",
//         "duration": "03:00:00",
//         "exam_name": "sem1"
//     },
//     {
//         "exam_id": 4,
//         "exam_date": "2024-03-10",
//         "start_time": "09:00:00",
//         "end_time": "12:00:00",
//         "duration": "03:00:00",
//         "exam_name": "sem2"
//     },
//     {
//         "exam_id": 5,
//         "exam_date": "2024-03-25",
//         "start_time": "13:30:00",
//         "end_time": "16:30:00",
//         "duration": "03:00:00",
//         "exam_name": "sem3"
//     },
//     {
//         "exam_id": 2,
//         "exam_date": "2024-02-01",
//         "start_time": "10:30:00",
//         "end_time": "13:30:00",
//         "duration": "03:00:00",
//         "exam_name": "sem4"
//     },
//     {
//         "exam_id": 3,
//         "exam_date": "2024-02-15",
//         "start_time": "14:00:00",
//         "end_time": "17:00:00",
//         "duration": "03:00:00",
//         "exam_name": "sem5"
//     }
// ]
// console.log(exams[1])

(async () =>{
    let response = await fetch('/examlist');
    exams = await response.json();
    for (i of exams) {
        var newdiv = document.createElement('div')
        newdiv.id = i.exam_id
        newdiv.innerText = i.exam_name
        let div = document.querySelector(".data")
        div.append(newdiv)
    }
})();

// getlist()



// let div = document.querySelector(".data")
// console.log(div)
// let newdiv = document.createElement('div')
// console.log(newdiv)
// newdiv.innerText = ' hi '
// div.append(newdiv)