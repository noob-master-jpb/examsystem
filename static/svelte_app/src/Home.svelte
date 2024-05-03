<script>
import { onMount } from "svelte";

let exam_list = []
let student_list = []

async function examlist(){
    let response = await fetch('/examlist');
    exam_list = await response.json();
	}
async function studentlist(){
    let response = await fetch('/studentlist');
    student_list = await response.json();
    }

onMount(examlist)
onMount(studentlist)
</script>

<input type="search" name="Search" id="search" placeholder="Search">
<div class="homepage">
    <div class="exam_home">
        <div id="exam_list_heading">Exam List</div>
            <div class = "exams" id="exam1">
            <div class="exam_id">Exam id</div> 
            <div class="exam_name">Exam name</div>
            <div class = 'date'>date</div> 
            <div class ='time'>time</div>
            <div class = 'duration'>Duration</div>
            <button>more</button>
    </div>
        
        {#each exam_list as exams}
        <div class = "exams" id="{exams.exam_id}">
        <div class = "exam_id"> ID:{exams.exam_id} </div>
        <div class = "exam_name">{exams.exam_name} </div>
        <div class = 'date'>{exams.exam_date} </div>
        <div class = 'time'>{exams.start_time} </div>
        <div class = 'duration'>{exams.duration} </div>
        <button class='Hold' id = {exams.exam_id}>Hold</button>
        <button class="Suspend" id = {exams.exam_id}>Suspend</button>
        <button class="Delete" id = {exams.exam_id}>Delete</button>
    </div>
        {/each}
    </div>

    <div class="user_home">
        <div id="user_list_heading">Students</div>
        <div class = 'users'id="user1">User 1 @1125</div>
        {#each student_list as student}
        <div class='users' id="{student.username}">{student.name}@{student.student_id}</div>
        {/each}
    </div>
</div>

<style>

#search{
    background-color:rgb(235,235,235);
    margin: 5px 7.5px;
    height: 5%;
    width: calc(100% - 15px);
    border-radius: 5px;
}



.homepage{
    display: flex;
    margin: 5px;
    height: calc(100% - 57.8px);
    width: calc(100% - 10px);

}



.exam_home{
    flex:.8;
    display: flex;
    border-radius: 5px;
    flex-direction: column;
    background-color:rgb(235,235,235);
    margin: 2.5px;
    overflow-y:auto;
}

#exam_list_heading{
    padding: 5px;
    justify-content: center;
    font-size: larger;
    position:sticky;
    top: 0;
    background-color: rgb(235,235,235);
}



.exams{
    display: grid;
    grid-template-columns: 20% 25% 10% 10% 10% 8% 8% 8%;
    margin: 2px;
    padding: 10px;
    /*background-color: rgb(215, 215, 215);*/
    border-color: gray;/* top & bottom, single line */
    border-style:solid;
    border-width: 0 0 1px 0;
}
.exams button{
    margin: 0 5px;
}

.exams button{
    align-self: center;
    border: none;
    padding: 3px;
    /* background-color: rgb(0, 0, 0, 0); */
    /* background-color: ; */
}

#user_list_heading{
    padding: 5px;
    justify-content: center;
    font-size: larger;
    position:sticky;
    top: 0;
    background-color: beige;
}

.user_home{
    flex: .2;
    display: flex;
    flex-direction: column;
    border-radius: 5px;
    background-color: beige;
    margin: 2.5px;
    overflow-y:auto;
}

.users{
    margin: 2px 5px;
    padding:  10px;
    /*background-color: rgb(215, 215, 215);*/
    border-color: gray;/* top & bottom, single line */
    border-style:solid;
    border-width: 0 0 1px 0;
}

</style>

