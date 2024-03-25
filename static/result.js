function verify(){
    if (document.title == 'results'){
        console.log('done')
    }
}


async function result_exams(by){
    let response = await fetch(`/results/${by}`)
    data = await response.json()
    
    result_area = document.querySelector('.result_list')

    for (i of data){
        if (i.exam_status != 'finished'){
            continue;
        }
        var result_div = document.createElement('div')
        result_div.className = 'result_exam'
        result_div.id = 'exam' + i.exam_id
        
        var data_div = document.createElement('div')
        data_div.className = 'data_exam'
        data_div.id = 'data_exam' + i.exam_id
        data_div.innerText = i.exam_name

        var info_div = document.createElement('div')
        info_div.className = 'info_exam'
        info_div.id = 'info_exam' + i.exam_id
        info_div.innerHTML = `attendence:${i.exam_attend}`

        result_div.append(data_div,info_div)
        result_area.append(result_div)
        
    }
}

result_exams('exams')