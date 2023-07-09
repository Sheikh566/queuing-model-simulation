
import { writable } from 'svelte/store'

export const simulationTableResponse = writable(null);
export const showAlert = writable(false);
export const showLoader = writable(false);