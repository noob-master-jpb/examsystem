<script>
import { onMount } from "svelte";


let student_list = []

async function studentlist(){
    let response = await fetch('/studentlist');
    student_list = await response.json();
}
onMount(studentlist)
</script>


<input type="search" name="Search" id="search" placeholder="Search">

<div class="studentlist">
    <div class="student">
        <div class="username">Username</div>
        <div class="name">Name</div>
        <div class="student_id">student id</div>
        <div class="registration_id">registration_id</div>
        <div class="dob">XXXX-XX-XX</div>
        <div class="course">Course</div>
        <div class="status">Active</div>
    </div>
    {#each student_list as student}
        <div class="student" id={student.username}>
            <div class="username">{student.username}</div>
            <div class="name">{student.name}</div>
            <div class="student_id">{student.student_id}</div>
            <div class="registration_id">{student.reg_id}</div>
            <div class="dob">{student.dob}</div>
            <div class="course">{student.course}</div>
            <div class="status">{student.status}</div>
        </div>
    {/each}
</div>




<style >

.studentlist{
    height: calc(100% - 57.8px);
       border-radius: 5px;
    flex-direction: column;
    background-color:rgb(235,235,235);
    margin: 5px;
    overflow-y:auto;
}

.student{
    display: grid;
    grid-template-columns: 20% 20% 10% 20% 10% 10% 10% ;
    margin: 2px 2px;
    padding:  10px;
    /*background-color: rgb(215, 215, 215);*/
    border-color: gray;/* top & bottom, single line */
    border-style:solid;
    border-width: 0 0 1px 0;
}


</style>