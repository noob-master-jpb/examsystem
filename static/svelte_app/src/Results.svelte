<script>
    import { onMount } from "svelte";

let result_list=[]

async function resultlist(){
    let response = await fetch('/resultlist');
    result_list = await response.json();
}

onMount(resultlist)
</script>

<input type="search" name="Search" id="search" placeholder="Search">
<div class="result_list">
    <div class="result_exam" id = 'exam1'>
        <div class="Exam_name">Exam_name </div>
        <div class="Exam_id"> exam_id</div>
        <div class = 'Date'>Date </div> 
        <div class="Attendence"> Attendence</div>
        <div class="status">status</div>
        <button class = 'btn_view_result' id = 'btn_view_result_1'>result</button> 
    </div>
    {#each result_list as result}
    <div class="result_exam" id = '{result.exam_id}'>
        <div class="Exam_name">{result.exam_name}</div>
        <div class="Exam_id">{result.exam_id}</div>
        <div class = 'Date'>{result.exam_date} </div> 
        <div class="Attendence"> {result.attendance}</div>
        <div class="status">status</div>
        <button class = 'btn_view_result' id = '{result.exam_id}'>view result</button> 
    </div>

    {/each}
</div>


<style>


.result_list{
    /* flex:.8; */
    display: flex;
    height: calc(100% - 57.8px);
    flex-direction: column;
    background-color:rgb(235,235,235);
    margin: 5px;
    border-radius: 5px;
    overflow-y:auto;
}

.result_exam{
    display: grid;
    grid-template-columns: 20% 20% 20% 20% 10% 10% ;
    margin: 2px 2px;
    padding:  0px;
    /*background-color: rgb(215, 215, 215);*/
    border-color: gray;/* top & bottom, single line */
    border-style:solid;
    border-width: 0 0 1px 0;
}
</style>