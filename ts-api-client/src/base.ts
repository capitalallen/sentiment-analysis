import fetch from 'isomorphic-unfetch'

type Config = {
    apiKey: string,
}

export abstract class Base {
    private apiKey: string = "";
    private basePath: string;
    constructor(config?: Config) {
        if (config){
            this.apiKey = config.apiKey || "";
        }
        this.basePath = 'http://127.0.0.1:5000/';
    }
    
    protected async request<T> (endpoint: string, options?: RequestInit): Promise<T> {
        const url = this.basePath + endpoint
        const headers = {
            'Content-type': 'application/json'
        }

        const config = {
            ...options,
            headers,
        }
        const r = await fetch(url, config)
        if (r.ok) {
            return r.json()
        }
        throw new Error(r.statusText)
    }
}