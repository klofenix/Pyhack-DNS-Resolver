![Supported Python versions](https://img.shields.io/badge/python->v3.0-blue.svg)

# PyHack-DNS-Resolver

## (aun en fase de creación)

- Utilidad creada en python para realizar analisis rapidos de DNS con fines de ser empleados en auditorias o pentesting.
- Para dar uso (de momento) modifica el archivo en la linea 5 el dominio a auditar XXXX.com.
- Proximamente se incluira una interfaza grafica interactiva.

<table summary="" id="" class="defaultstyle bx--data-table"><caption class="bx--data-table-header"><span class="tablecap bx--data-table-header__title">Tabla Tipos de consulta DNS </span></caption><colgroup><col style="width:30.303030303030305%"><col style="width:69.6969696969697%"></colgroup><thead style="text-align:left;">
<tr>
<th id="d154260e217"><div class="bx--table-header-label">Código de consulta </div></th>
<th id="d154260e220"><div class="bx--table-header-label">Tipo de consulta </div></th>

</tr>

</thead>
<tbody>
<tr>
<td headers="d154260e217 "><code class="ph codeph">A</code></td>

<td headers="d154260e220 ">Dirección de host </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">NS </code></td>

<td headers="d154260e220 ">Servidor de nombres autorizado </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">MD </code></td>

<td headers="d154260e220 ">Destino de correo  </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">MF </code></td>

<td headers="d154260e220 ">Reenviador de correo </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">CNAME </code></td>

<td headers="d154260e220 ">Nombre canónico para un alias </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">SOA </code></td>

<td headers="d154260e220 ">Inicio de una zona de autorización </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">MB </code></td>

<td headers="d154260e220 ">Nombre de dominio de buzón </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">MG </code></td>

<td headers="d154260e220 ">Miembro de grupo de correo </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">MR </code></td>

<td headers="d154260e220 ">Nombre de dominio de redenominación de correo </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">NULL </code></td>

<td headers="d154260e220 ">RR nulo </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">WKS </code></td>

<td headers="d154260e220 ">Descripción de servicio conocido </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">PTR </code></td>

<td headers="d154260e220 "> Puntero de nombre de dominio </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">HINFO </code></td>

<td headers="d154260e220 ">Información de host </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">MINFO </code></td>

<td headers="d154260e220 ">Información de lista de buzón o correo </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">MX </code></td>

<td headers="d154260e220 ">Intercambio de correo </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">TXT </code></td>

<td headers="d154260e220 "> Cadenas de texto </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">AXFR </code></td>

<td headers="d154260e220 ">Transferencia de una zona entera </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">MAILB </code></td>

<td headers="d154260e220 "> Registros relacionados con el buzón </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">MAILA </code></td>

<td headers="d154260e220 ">RR de agente de correo </td>

</tr>

<tr>
<td headers="d154260e217 "><code class="ph codeph">ANY </code></td>

<td headers="d154260e220 ">Todos los registros </td>

</tr>

</tbody>
</table>
