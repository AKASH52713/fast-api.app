import api from "./api";
import type { Job } from "../types/job";
import type { Company } from "../types/company";

export async function getJobs(): Promise<Job[]> {
    const response = await api.get(`/job`);
    return response.data;
}

export async function getJob(id:string): Promise<Job> {
    const response = await api.get(`/job/${id}`);
    return response.data;
}

export async function createJob(job  : Job): Promise<Job> {
    const response = await api.post(`/job`, job);
    return response.data;
}

export async function updateJob(id: string, job: Job): Promise<Job> {
    const response = await api.put(`/job/${id}`, job);
    return response.data;
}

export async function deleteJob (id: string): Promise<Job> {
    const response = await api.delete(`/job/${id}`);
    return response.data;
}
