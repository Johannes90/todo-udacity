import axios from 'axios';

export let authCall = axios.create({
    baseURL: 'http://127.0.0.1:8080/api',
    headers: { 
        'Content-Type': 'application/json', 
        'Authorization': "JWT " + localStorage.getItem("access_token")
    }
});


export let noAuthCall = axios.create({
    baseURL: 'http://127.0.0.1:8080/api',
    headers: { 
        'Content-Type': 'application/json'
    }
});