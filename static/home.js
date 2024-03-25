function verify(){
    if (document.title == 'Home'){
        console.log('done')
    }
}

// verify()

// (async () =>{
//     let response = await fetch('/examlist');
//     exams = await response.json();
//     for (i of exams) {
//         var newdiv = document.createElement('div')
//         newdiv.id = i.exam_id
//         newdiv.innerText = i.exam_name
//         let div = document.querySelector(".data")
//         div.append(newdiv)
//     }
// })();



// exams = [
//     {
//         "exam_id": 1,
//         "exam_date": "2024-01-15",
//         "start_time": "09:00:00",
//         "end_time": "12:00:00",
//         "duration": "03:00:00",
//         "exam_name": "sem1"
// }
// ]
// function make(exams){
//     let exam_area = document.querySelector(".exam_home") 
//     for (i of exams){
//         var listdiv = document.createElement('div')
//         listdiv.className = 'exam_list'
//         listdiv.id = 'exam' + String(i.exam_id)

//         var datadiv = document.createElement('div')
//         datadiv.className = 'data_exam'
//         datadiv.id = 'data_exam' + String(i.exam_id)
//         datadiv.innerText = i.exam_name

//         var infodiv = document.createElement('div')
//         infodiv.className = 'info_exam'
//         infodiv.id = 'info_exam' + String(i.exam_id)
//         infodiv.innerHTML = `date:${i.exam_date} <br> Time:${i.start_time} <br> Duration: ${i.duration}`

//         var button = document.createElement('button')
//         button.innerText='more'

//         listdiv.append(datadiv,infodiv,button)

//         // let target = document.querySelector('.exam_home')
//         exam_area.append(listdiv)

//     }

    
// }

(async () => {
    let response = await fetch('/examlist');
    exams = await response.json();
    // console.log(exams)
    let exam_area = document.querySelector(".exam_home") 
    for (i of exams){
        var listdiv = document.createElement('div')
        listdiv.className = 'exams'
        listdiv.id = 'exam' + String(i.exam_id)

        var datadiv = document.createElement('div')
        datadiv.className = 'data_exam'
        datadiv.id = 'data_exam' + String(i.exam_id)
        datadiv.innerText = i.exam_name

        var infodiv = document.createElement('div')
        infodiv.className = 'info_exam'
        infodiv.id = 'info_exam' + String(i.exam_id)
        infodiv.innerHTML = `date:${i.exam_date} <br> Time:${i.start_time} <br> Duration: ${i.duration}`

        var button = document.createElement('button')
        button.innerText='more'

        listdiv.append(datadiv,infodiv,button)

        // let target = document.querySelector('.exam_home')
        exam_area.append(listdiv)

    }
})();


(async () => {
    let response = await fetch('/userlist')
    users = await response.json();
    let user_area = document.querySelector('.user_home')
    // console.log(users)
    for (i of users){
        var user_div = document.createElement('div')
        user_div.className = 'user_list'
        user_div.id = i.student_id
        user_div.innerText= i.name + '@' + i.student_id
        user_area.append(user_div)
    }
})();