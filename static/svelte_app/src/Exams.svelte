<script>
    import { onMount } from "svelte";
    import Win_new_exam from "./New_exam.svelte";
    import Win_edit_exam from "./indi_exam.svelte";

    let exam_list = []
    let show_new_exam = false;
    let exam_form={}
    let show_edit_exam = false;
    let edit_exam_data= {};
 

    async function examlist(){
        let response = await fetch('/examlist');
        exam_list = await response.json();
        }

    const handle_win_new_exam = () => {
        show_new_exam = !show_new_exam 
    }

    const handle_edit_exam = (id) => {
        edit_exam_data = exam_list.find((exams) => exams.exam_id === id);
        show_edit_exam = !show_edit_exam;
    }

    
    onMount(examlist)
</script>



<input type="search" name="Search" id="search" placeholder="Search">

<div id="options">
    <div id="opt_new_exam" on:click={() => handle_win_new_exam()} on:keydown>New exam</div>
</div>

        <Win_new_exam show_new_exam={show_new_exam} on:click={() => handle_win_new_exam()} handle_win_new_exam={async () => handle_win_new_exam()} />
        {#if show_edit_exam}
        <Win_edit_exam examdata = {edit_exam_data} {show_edit_exam} {handle_edit_exam}/>
        {/if}
<div class="exam_list">
    
    <div class = "exams" id="exam1">
        <div class="exam_id">Exam id</div> 
        <div class="exam_name">Exam name</div>
        <div class = 'date'>date</div> 
        <div class ='time'>time</div>
        <div class = 'duration'>Duration</div>
        <div class="status">status</div>
        <div class="option" >option</div>
    </div>
    {#each exam_list as exams}
    <div class = "exams" id="{exams.exam_id}">
        <div class = "exam_id"> ID:{exams.exam_id} </div>
        <div class = "exam_name">{exams.exam_name} </div>
        <div class = 'date'>{exams.exam_date} </div>
        <div class = 'time'>{exams.start_time} </div>
        <div class = 'duration'>{exams.duration} </div>
        <div class="status">{exams.exam_status}</div>
        <button class="edit" id = {exams.exam_id} on:click={() => {handle_edit_exam(exams.exam_id)}}>edit</button>
        <button class=" border-none">❌</button>
    </div>
    {/each}
</div>

<style>
#options{
    margin: 5px;
    width: calc(100% - 10px);
    
}

#options div{
    background-color:rgb(235,235,235);
    border-radius: 5px;
    padding: 5px;
    width: fit-content;

}

#options div:hover{
    cursor: pointer;
    background-color: lightgrey;
}

.exams{
    display: grid;
    grid-template-columns: 20% 20% 12% 12% 12% 12% 8% 4%;
    margin: 2px 2px;
    padding:  5px;
    /*background-color: rgb(215, 215, 215);*/
    border-color: gray;/* top & bottom, single line */
    border-style:solid;
    border-width: 0 0 1px 0;
}



.exams button{
    padding: 0 auto;
    margin: 0 0 5px 0;
    max-width: 90%;
    min-width:max-content;
    max-height: initial;
}

.exam_list{
    display: flex;
    height: calc(100% - 57.8px);
    border-radius: 5px;
    flex-direction: column;
    background-color:rgb(235,235,235);
    margin: 5px;
    min-width: 800px;
    overflow-y:auto;
}

     
</style>