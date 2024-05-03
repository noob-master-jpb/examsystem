<script>
    import { onMount } from 'svelte';
  

    var today = new Date().toISOString().split('T')[0];

    let currentTime = '';
    export let show_new_exam ;

    export let handle_win_new_exam;

    let handleSubmit = async(form) =>{
            exam_form = form

            for (i of form.course_list){
                exam_form.course_list[i] = true
            }
            console.log(form)
            let response = await fetch('/newexam', {
                method: 'POST',
                headers: {
                'Content-Type':'application/json'
                    },
                body: JSON.stringify(exam_form),
            })
            let data = await response.json()
            console.log(data)
            handle_win_new_exam()
            exam_form = {
                        name:null,
                        date:null,
                        time:null,
                        duration:null,
                        status:"live",
                        course_list:{}
                        }
            }
    


    let exam_form = {
        name:null,
        date:null,
        time:null,
        duration:null,
        status:"live",
        course_list:{}
                }
    onMount(() => {
        const now = new Date();
        const hours = now.getHours().toString().padStart(2, '0');
        const minutes = now.getMinutes().toString().padStart(2, '0');
        currentTime = `${hours}:${minutes}`;
    }); 

</script>
{#if show_new_exam}
    <div class="backdrop">
        <form on:submit|preventDefault={() => handleSubmit(exam_form)}>
            
            <div id = 'exam_details'>
                <input type="text" name="inp_exam_name" id="id_exam_name" placeholder="Exam Name" bind:value ={exam_form.name}>
                <label for="id_exam_time">Select a Date:</label> 
                <input type="date" name="inp_exam_date" id="id_exam_date" min={today} bind:value={exam_form.date}>
                <label for="id_exam_time">Select a time:</label> 
                <input type="time" name="inp_exam_time" id="id_exam_time" min={currentTime} class=" ml-auto w-full" bind:value={exam_form.time} >

                <div id="id_exam_duration">Duration:
                    <input type="number" min = '0' max = '3' placeholder="Hours"> <input type="number" min = '00' max = '59' placeholder="Minutes" bind:value={exam_form.duration}>
                </div>

                <div id="exam_status" class="flex justify-around" >

                    <div class="radio_btn">
                        <input type="radio" name="exam_status" id="status_live" value="live" class=" hidden" checked="checked" bind:group={exam_form.status}>
                        <label for="status_live" class="white">Live</label>
                    </div>
                    <div class="radio_btn">
                        <input type="radio" name="exam_status" id="onwait" value="onwait" class=" hidden" bind:group={exam_form.status}>
                        <label for="onwait" class = "white">OnWait</label>
                    </div>
                </div>
            </div>


            <div id = 'course_list' class = " w-[calc(49%)]">
                <div class="checkbox_div">
                    <input type="checkbox" id="CCA" name="CCA" value="CCA" bind:checked={exam_form.course_list.CCA}><label for="CCA" >CCA</label><span></span>
                </div>
                <div class="checkbox_div">
                    <input type="checkbox" id="DCA" name="DCA" value="DCA" bind:checked={exam_form.course_list.DCA}><label for="DCA">DCA</label><span></span>
                </div>
                <div class="checkbox_div">
                    <input type="checkbox" id="PGDCA" name="PGDCA" value="PGDCA" bind:checked={exam_form.course_list.PGDCA}><label for="PGDCA">PGDCA</label><span></span>
                </div>
                <div class="checkbox_div">
                    <input type="checkbox" id="CDTP" name="CDTP" value="CDTP" bind:checked={exam_form.course_list.CDTP}><label for="CDTP">CDTP</label><span></span>
                </div>
                <div class="checkbox_div">
                    <input type="checkbox" id="DDTP" name="DDTP" value="DDTP" bind:checked={exam_form.course_list.DDTP}><label for="DDTP">DDTP</label><span></span>
                </div>
                <div class="checkbox_div">
                    <input type="checkbox" id="ADTP" name="ADTP" value="ADTP" bind:checked={exam_form.course_list.ADTP}><label for="ADTP">ADTP</label><span></span>
                </div>
                <div class="checkbox_div">
                    <input type="checkbox" id="CFA" name="CFA" value="CFA" bind:checked={exam_form.course_list.CFA}><label for="CFA">CFA</label><span></span>
                </div>
                <div class="checkbox_div">
                    <input type="checkbox" id="DFA" name="DFA" value="DFA" bind:checked={exam_form.course_list.DFA}><label for="DFA">DFA</label><span></span>
                </div>
                <div class="checkbox_div">
                    <input type="checkbox" id="CMM" name="CMM" value="CMM" bind:checked={exam_form.course_list.CMM}><label for="CMM">CMM</label><span></span>
                </div>
                <div class="checkbox_div">
                    <input type="checkbox" id="DMM" name="DMM" value="DMM" bind:checked={exam_form.course_list.DMM}><label for="DMM">DMM</label><span></span>
                </div>
                <div class="checkbox_div">
                    <input type="checkbox" id="CWD" name="CWD" value="CWD" bind:checked={exam_form.course_list.CWD}><label for="CWD">CWD</label><span></span>
                </div>
                <div class="checkbox_div">
                    <input type="checkbox" id="DWD" name="DWD" value="DWD" bind:checked={exam_form.course_list.DWD}><label for="DWD">DWD</label><span></span>
                </div>
                <div class="checkbox_div">
                    <input type="checkbox" id="DCTT" name="DCTT" value="DCTT" bind:checked={exam_form.course_list.DCTT}><label for="DCTT">DCTT</label><span></span>
                </div>
                <div class="checkbox_div">
                    <input type="checkbox" id="Sch" name="Sch" value="Sch" bind:checked={exam_form.course_list.Sch}><label for="Sch">Sch</label><span></span>
                </div>
                
            </div>




            <div id="btns_confirm" >
            <button type="submit" style="cursor: pointer; " class = "hover:border-2 hover:border-gray-600" on:click{handle_win_new_exam}>Create</button>
            <div id="cancel" on:click on:keypress={handle_win_new_exam}> Cancel</div>
            </div>
        </form>
        
    </div>
{/if}

<style>
    .backdrop {
        position: absolute;
        height: 100%;
        width: 100%;
        background-color: rgba(210, 210, 210, 60%);
        backdrop-filter: blur(2px);
        top: 0;
        left: 0;
        }




    form{
        position: absolute;
        top: calc(50% - 40%);
        left: calc(50% - 17.5%);
        height: 70%;
        width: 35%;
        background-color: white;
        text-decoration: none;
        padding: 10px;
        border-radius: 10px;
        display: flex;
        min-width: 500px;
    }

    #id_exam_name,
    #id_exam_date{
        width: 100%;
    }

    #exam_status div{
        width: 30%;
        text-align: center;
        border-radius: 5px;

    }

    .radio_btn label{
        width: 100%;
        border-radius: 5px;
        padding: 5px;
        height: 100%;
        border: 2px solid gray ;

    }

    #exam_status input:checked + label{
    border: none;
    border-radius: 5px;
    }

    #status_live:checked + label{
        background-color: limegreen;
    }

    #onwait:checked + label{
        background-color: grey;
    }



    #btns_confirm{
        display: flex;
        flex-direction: column;
        position: absolute;
        top:100%;
        left: 0%;
        width: 100%;
        padding: 5px 0;
    }
    #btns_confirm button{
        width: 100%;
        border-radius: 5px;

    }

    #course_list, #exam_details{
        width: 100%;
    }

    .checkbox_div{
        display: grid;
        grid-template-columns: 30% 70%;
    }
    .checkbox_div input{
        display: none;

    }
    .checkbox_div label{
        -webkit-touch-callout: none;
        -webkit-user-select: none;
        -khtml-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        padding: 4px 4px;
        margin: 2px 0px 2px 10px;
        border-radius: 5px;
        
    }

    .checkbox_div label:hover{
        background-color:lightgray;
    }

    .checkbox_div input:checked+label{
        border:2px solid gray;
        border-radius: 5px;
        padding: 2.5px 2px;
    }
 
    .checkbox_div input[type="checkbox"] + label + span::after {
        content: "not selected"; 
        color: lightslategray ;
    } 
    
    .checkbox_div input[type="checkbox"]:checked + label + span::after {
        content: "click to upload qustion";
        
    }
    .checkbox_div span{
        height: max-content;
        padding: 2px;
        margin: 2px 0px 2px 1px;  
        text-wrap: wrap;
        font-size: 100%;
        text-align: center;
    }


    #cancel{ 
        width: 100%;
        padding: 10px;
        text-align: center;
        border: 2px solid grey;
        border-radius: 5px;

        
    }    
    #cancel:hover{
        background-color: rgba(255, 255, 255, 60%);
        cursor:no-drop ;
    }
</style>