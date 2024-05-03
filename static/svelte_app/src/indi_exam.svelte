<script>
    import { onMount } from "svelte";
</script>

<div id="backdrop">
    <div id="exampage">
        <div id="examdetails">
            <div id="exam_id" class="">Exam id : 151269426</div>
            <div id="examname">Exam name: SEM1</div>
            <div id="date">Date: 2022-10-10</div>
            <div id="time">Time: 12:00:00</div>
            <div id="duration">Duration: 12:00:00</div>
        </div>
        
    </div>
</div>


<style>
    #backdrop {
        position: absolute;
        height: 100%;
        width: 100%;
        background-color: rgba(210, 210, 210, 60%);
        backdrop-filter: blur(2px);
        top: 0;
        left: 0;
        }
    
    #exampage{
        position: absolute;
        top: calc(50% - 25%);
        left: calc(50% - 20%);
        height: 50%;
        width: 40%;
        background-color: white;
        text-decoration: none;
        padding: 10px;
        border-radius: 10px;
        display: flex;
        /* min-width: 500px; */
    }
    #examdetails{
        margin: 2px;
        padding: 2px;
        width: 100%;
        border: 1px solid; 
    }

    
</style>