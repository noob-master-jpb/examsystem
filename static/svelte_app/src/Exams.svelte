<script>
    import { onMount } from "svelte";
    import Win_new_exam from "./New_exam.svelte";
    import Win_indi_exam from "./indi_exam.svelte";

    let exam_list = []
    let show_new_exam = false;
    let exam_form={}
    let show_each_exam = !false;

    async function examlist(){
        let response = await fetch('/examlist');
        exam_list = await response.json();
        }

    const handle_win_new_exam = () => {
        show_new_exam = !show_new_exam
    }
    
    onMount(examlist)
</script>



<input type="search" name="Search" id="search" placeholder="Search">

<div id="options">
    <div id="opt_new_exam" on:click={() => handle_win_new_exam()} on:keydown>New exam</div>
</div>

        <Win_new_exam show_new_exam={show_new_exam} on:click={() => handle_win_new_exam()} handle_win_new_exam={() => handle_win_new_exam()} />
        {#if show_each_exam}
        <Win_indi_exam/>
        {/if}
<div class="exam_list">
    
    <div class = "exams" id="exam1">
        <div class="exam_id">Exam id</div> 
        <div class="exam_name">Exam name</div>
        <div class = 'date'>date</div> 
        <div class ='time'>time</div>
        <div class = 'duration'>Duration</div>
        <div class="status">status</div>
        <button class="Delete" >Delete</button>
    </div>
    {#each exam_list as exams}
    <div class = "exams" id="{exams.exam_id}">
        <div class = "exam_id"> ID:{exams.exam_id} </div>
        <div class = "exam_name">{exams.exam_name} </div>
        <div class = 'date'>{exams.exam_date} </div>
        <div class = 'time'>{exams.start_time} </div>
        <div class = 'duration'>{exams.duration} </div>
        <div class="status">{exams.exam_status}</div>
        <button class="Delete" id = {exams.exam_id}>Delete</button>
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
}

.exams{
    display: grid;
    grid-template-columns: 22% 22% 12% 12% 12% 12% 8% ;
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