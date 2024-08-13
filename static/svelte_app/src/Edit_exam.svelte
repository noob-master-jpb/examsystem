<script>
    import { onMount } from "svelte";
    

    var today = new Date().toISOString().split('T')[0];
    export let examdata;
    export let show_edit_exam;
    export let handle_edit_exam;
    let duration_hrs = String(examdata.duration).slice(0,2)
    let duration_min = String(examdata.duration).slice(3,5)

    let handleupdate = async(examdata) =>{
            console.log(examdata)
            examdata.duration = String(duration_hrs)+":" + String(duration_min) + ":00"
            let response = await fetch('/update_exam', {
                method: 'PUT',
                headers: {
                'Content-Type':'application/json'
                    },
                body: JSON.stringify(examdata),
            })

            handle_edit_exam()
            };
            
            

    onMount(() => {
        const now = new Date();
        const hours = now.getHours().toString().padStart(2, '0');
        const minutes = now.getMinutes().toString().padStart(2, '0');
        let currentTime = `${hours}:${minutes}`;
        
    }); 
</script>

{#if show_edit_exam}
    <div id="backdrop">
        <form on:submit|preventDefault={() => handleupdate(examdata)}>
            <div id="exampage" >
                <div id="examdetails">
                    <div id="exam_identity">
                        <div id="exam_id" class=" text-xl p-1">{examdata.exam_id}</div>
                    </div>
                    <div id="options">
                        <div id="exam_timing">
                            <b>Change Name</b> 
                            <input type="text" name="inp_exam_name" id="id_exam_name" placeholder="Exam Name" bind:value ={examdata.exam_name}>
                            <label for="id_exam_time"><b>Change Date:</b></label> 
                            <input type="date" name="inp_exam_date" id="id_exam_date" min={today} bind:value={examdata.exam_date}>
                            <label for="id_exam_time"> <b>Change Time:</b></label> 
                            <input type="time" name="inp_exam_time" id="id_exam_time" class=" ml-auto w-1/3" bind:value= {examdata.start_time}>
                            <div><b>Change Duration</b></div>
                            <input type="number" min = '0' max = '3' bind:value={duration_hrs} placeholder="Hours">
                            <input type="number" min = '00' max = '59' placeholder="Minutes" bind:value={duration_min}>
                            
                        </div>
                        <b>Status</b>
                        <div id="exam_status" class="flex justify-around" >
                            {#if examdata.exam_status == 'live'}
                            <div class="radio_btn">
                                <input type="radio" name="exam_status" id="status_live" value="live" class=" hidden" checked="checked">
                                <label for="status_live" class="white">Live</label>
                            </div>
                            
                            <div class="radio_btn">
                                <input type="radio" name="exam_status" id="onwait" value="onwait" class=" hidden" >
                                <label for="onwait" class = "white">OnWait</label>
                            </div>
                            {:else if examdata.exam_status == 'onwait'}
                            <div class="radio_btn">
                                <input type="radio" name="exam_status" id="status_live" value="live" class=" hidden">
                                <label for="status_live" class="white">Live</label>
                            </div>
                            
                            <div class="radio_btn">
                                <input type="radio" name="exam_status" id="onwait" value="onwait" class=" hidden"  checked="checked">
                                <label for="onwait" class = "white">OnWait</label>
                            </div>
                            {:else}
                            <div class="radio_btn">
                                <input type="radio" name="exam_status" id="status_live" value="live" class=" hidden">
                                <label for="status_live" class="white">Live</label>
                            </div>
                            
                            <div class="radio_btn">
                                <input type="radio" name="exam_status" id="onwait" value="onwait" class=" hidden">
                                <label for="onwait" class = "white">OnWait</label>
                            </div>
                            {/if}
                        </div>
                    </div>
                    <div id="confirm" class = "flex flex-col justify-items-center text-center p-8">
                        <button type="submit" on:click={() => handle_edit_exam}>confirm</button>
                    </div>
                    
                        <button type="reset" id="close" on:click={handle_edit_exam()} >❌</button>
                    
                </div>
                
            </div>
        </form>
    </div>
{/if}

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
        left: calc(50% - 10%);
        height: 50%;
        width: 20%;
        background-color: white;
        text-decoration: none;
        /* padding: 10px; */
        border-radius: 10px;
        display: flex;
        min-width: 300px;
    }
    #examdetails{
        margin: 2px;
        padding: 2px;
        width: 100%;
        /* border: 1px solid;  */
    }

    #exam_identity{
        display: flex;
        justify-content: space-around;
    }

    #options{
        text-align: center;
    }

    #exam_status{
        display: flex;
        /* flex-direction: column; */
        margin: 2px;

    }
    #exam_status div{
        width: 30%;
        text-align: center;
        /* border-radius: 5px; */
        
    }

    .radio_btn label{
        width: 100%;
        border-radius: 5px;
        padding: 5px;
        height: 100%;
        border: 2px solid gray ;

    }

    #exam_status input:checked + label{
    border-radius: 5px;
    }

    #status_live:checked + label{
        background-color: limegreen;
        border: 2px solid limegreen;
    }

    #onwait:checked + label{
        background-color: grey;
        border: 1px solid grey ;
    }

    #close{
        position: absolute;
        /* top: calc(50% - 32%); */
        /* left: calc(50% + 10%); */
        top: 0;
        right: 0;
        /* width: 25px; */
        /* height: 25px; */
        background: none;
        text-decoration: none;
        border: none;
    }
</style>
