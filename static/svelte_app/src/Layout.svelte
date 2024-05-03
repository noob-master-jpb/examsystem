<!-- Layout.svelte -->
<script>
    import Router  from 'svelte-spa-router';
    import Route from 'svelte-spa-router'; // Note: Import Route separately

    import Home from './Home.svelte';
    import Exams from './Exams.svelte';
    import Results from './Results.svelte';
    import Students from './Students.svelte';

</script>


<Router>
    <Route path="/admin " component={Home} />
    <Route path="/exams" component={Exams} />
    <Route path="/results" component={Results} />
    <Route path="/students" component={Students} />
</Router>
