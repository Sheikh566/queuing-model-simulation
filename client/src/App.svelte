<script>
  import Header from "./Header.svelte";
  import Form from "./Form.svelte";
  import Table from "./Table.svelte";
  import Footer from "./Footer.svelte";
  import { showAlert, simulationTableResponse, showLoader } from "./store";
  import { fly } from "svelte/transition";
  import Loader from "./Loader.svelte";

  const cumPropTableFields = ["Cumulative Probability Lookup", "Cumulative Probability", "Inter-Arrival"];
  const arrivalTableFields = [
    "OBS.",
    "RANDOM ARRIVAL",
    "INTER-ARRIVAL",
    "ARRIVAL TIME",
    "RANDOM SERVICE",
    "SERVICE TIME",
    "START TIME",
    "END TIME",
    "TURN AROUND TIME",
    "WAITING TIME",
    "RESPONSE TIME"
  ];
</script>

<div id="container">
  {#if $showAlert}
  <div class="alert-box" transition:fly={{ y: 200, duration: 1000 }}>
    <center>Something Went Wrong</center>
  </div>
  {/if}
  {#if $showLoader}
    <Loader />  
  {/if}
  <Header />
  <Form />
  {#if $simulationTableResponse?.simulationTable?.length && $showLoader == false}
    <h2>Inter-Arrival Lookup</h2>
    <Table fields={cumPropTableFields} isSimulationTable={false} data={$simulationTableResponse.cumulativeTable}/>
    <h2>Simulations</h2>
    <Table
      fields={arrivalTableFields}
      data={$simulationTableResponse.simulationTable}
    />
    <h2>Averages</h2>
    <Table
      fields={$simulationTableResponse.averages.map(a => a.name.toUpperCase())}
      data={[$simulationTableResponse.averages.map(a => a.value)]}
      isSimulationTable={false}
    /> 
  {/if}
  <Footer />
</div>

<svelte:head>
  <title>Queuing Simulator</title>
</svelte:head>

<style>
  #container {
    display: flex;
    align-items: center;
    flex-direction: column;
  }
  .alert-box {
    padding-top: 20px;
    padding-bottom: 20px;
    background-color: #f4433688;
    position: absolute;
    transform: translate(0, -20px);
    color: white;
    width: 500px;
}
</style>
