import Home from './Home.svelte';
import Exams from './Exams.svelte';
import Results from './Results.svelte';
import Students from './Students.svelte';

const routes = {
    '/admin': Home,
    '/admin/': Home,
    '/exams': Exams,
    '/results': Results,
    '/students': Students
};


const target = document.getElementById('content');
const path = window.location.pathname;

if (routes[path]) {
    new routes[path]({
        target
    });
} else {
    console.warn(`Nothing to render for path ${path}`);
}


