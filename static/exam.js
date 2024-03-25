function verify(){
    if (document.title == 'exams'){
        console.log('done')
    }
}


const examlist = async () => {
    let response = await fetch('/examlist');
    exams = await response.json();
    // console.log(exams)
    let exam_area = document.querySelector(".exam_list") 
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

        exam_area.append(listdiv)

    }
}

examlist()


