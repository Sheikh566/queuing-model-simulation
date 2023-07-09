<script>
  import { distributions, color } from "./lib/constants";
  import { showAlert, showLoader, simulationTableResponse } from "./store";

  // Form inputs
  let numOfServers,
    arrivalDistType,
    meanArrival,
    serviceDistType,
    meanService,
    varianceArrival,
    varianceService;

  $: arrivalVarianceDisabled = arrivalDistType == 0;
  $: serviceVarianceDisabled = serviceDistType == 0;


  const submitForm = async () => {
    console.log("Form Submitted");
    showLoader.set(true)
    try {
      const res = await fetch(
      "http://127.0.0.1:5000/get-complete-simulation?" +
        new URLSearchParams({
          numOfServers,
          arrivalDistType,
          meanArrival,
          serviceDistType,
          meanService,
          varianceArrival,
          varianceService,
        }),
        { headers: {
            "Access-Control-Allow-Origin": "*"
          }
        }
      );
    const data = await res.json();
    simulationTableResponse.set(data);
    } catch (error) {
      showAlert.set(true);
      setTimeout(() => { showAlert.set(false);}, 3000);
    }
    showLoader.set(false);
  };

</script>

<form on:submit|preventDefault={submitForm} class="form" style="opacity: {$showLoader ? 0.5 : 1};">
  <select bind:value={arrivalDistType} class="form-first" required>
    <option value="">Select Arrival Distribution</option>
    {#each distributions as d}
      <option value={d.val}>{d.name}</option>
    {/each}
  </select>
  <div class="form-name">
    <input
      class="form-first"
      type="number"
      placeholder="Arrival Mean"
      min="0"
      step="0.01"
      required
      bind:value={meanArrival}
    />
    <input
      class="form-last"
      type="number"
      placeholder="Arrival Variance"
      min="0"
      step="0.01"
      disabled={arrivalVarianceDisabled}
      bind:value={varianceArrival}
    />
  </div>
  <select bind:value={serviceDistType} class="form-first" required>
    <option value="">Select Service Distribution</option>
    {#each distributions as d}
      <option value={d.val}>{d.name}</option>
    {/each}
  </select>
  <div class="form-name">
    <input
      class="form-first"
      type="number"
      placeholder="Service Mean"
      min="0"
      step="0.01"
      required
      bind:value={meanService}
    />
    <input
      class="form-last"
      type="number"
      placeholder="Service Variance"
      min="0"
      step="0.01"
      disabled={serviceVarianceDisabled}
      bind:value={varianceService}
    />
  </div>
  <div class="form-name">
    <input
      class="form-first"
      type="number"
      placeholder="# Servers"
      min="1"
      required
      bind:value={numOfServers}
    />
  </div>
  <button type="submit" style="background-color: {color.secondary};" on:submit={submitForm}>Simulate</button>
</form>

<style>
  :root {
    --bg: rgb(175, 202, 192);
    --placeholder: rgb(70, 70, 70);
    --text: rgb(70, 70, 70);
  }

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  .form {
    width: min(500px, 90vw);
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin: 30px 0 30px 0;
  }

  .form * {
    width: 100%;
    padding: 1rem;
    font: 900 0.85rem futura, sans-serif;
    color: var(--text);
    text-transform: uppercase;
    background-color: rgba(255, 255, 255, 0.75);
    border: none;
    outline: 0;
  }

  ::placeholder {
    color: var(--placeholder);
  }

  input:focus {
    background-color: rgba(255, 255, 255, 0.5);
  }
  button:disabled, input:disabled {
    opacity: 0.5;
  }

  button:hover {
    background-color: #001122;
  }

  .form-name {
    display: flex;
    gap: 1rem;
    padding: 0;
    background-color: transparent;
  }

</style>
