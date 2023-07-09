<script>
  import { color } from "./lib/constants";

  export let fields = [];
  export let data = [[]];
  export let isSimulationTable = true;
</script>

<table >
  <tr>
    {#each fields as field}
      <th>{field}</th>
    {/each}
  </tr>
  <tbody style="background-color: {color.secondary};">
    {#each data as row, i }
    <tr>
      {#if isSimulationTable}
        <td>{i + 1}</td>
      {/if}
      {#each row as val }
        <td>{val % 1 === 0 ? val : val.toFixed(isSimulationTable ? 10 : 4 )}</td>
      {/each}
    </tr>
  {/each}
  </tbody>
</table>

<style>
:root {  
  --table-background-hue: 255;
  --table-background-saturation: 20%;
  --table-background-light: 20%;
  
  --th-opacity: 0.5;
  --th-2n: 0.15;
}

table {
  width: 100%;
  border-collapse: collapse;
  box-shadow: 5px 4px 7px 5px rgba(0, 0, 0, 0.2);
}

th, 
td {
  padding: 1rem;
}
td {
  color: black;
}

th {
  background: hsl(0 0% 0% / var(--th-opacity));
  text-transform: uppercase;
}

@media (max-width: 650px) {
  th {
    display: none;
  }
  
  td {
    display: grid;
    gap: 0.5rem;
    grid-template-columns: 18ch auto;
    padding: 0.5rem 1rem;
  }  
  

  td::before {
    content: attr(data-cell) ": ";
    font-weight: 700;
    text-transform: capitalize;
  }
}
</style>
