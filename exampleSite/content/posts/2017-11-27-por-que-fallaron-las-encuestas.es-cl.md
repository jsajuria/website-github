+++ 
title = "¿Por qué fallaron las encuestas?"
author = "Javier Sajuria"
date = "2017-11-27"
slug =  "por-que-fallaron-las-encuestas"
categories = ["Press", "Spanish"]
tags: ["Duna"]

+++

*Este post fue publicado originalmente en el sitio web de [Radio Duna][1]*

En algo que está pareciendo costumbre a lo largo del mundo, las encuestas en Chile fallaron en predecir el resultado de las elecciones presidenciales. Si bien cada encuesta tuvo distintos énfasis, los principales fallos se encuentran en la sobreestimación de los votos de Sebastián Piñera y en la subestimación de los votos de Beatriz Sánchez.

Entender qué pasó va a ser de las labores más complejas que tendrán que llevar a cabo los encuestadores nacionales en los próximos meses. **Con el ánimo de aportar al debate y, ojalá, abrir la conversación, me permito plantear algunas ideas de qué es lo que puede haber pasado y qué se puede hacer al respecto.** Estas observaciones son una mezcla de la experiencia internacional respecto a las fallas de las encuestas (algo muy común últimamente) y la poca evidencia que tenemos disponible en Chile.

### Construcción de muestras y error de medición

Las encuestas pueden tener, al menos, dos fuentes de error. La primera es el error muestral, es decir, la diferencia entre la población y la muestra. Cuando tenemos una muestra probabilística (donde todos los miembros de la población tienen la misma probabilidad de ser encuestados), entonces ese error es aleatorio. En términos simples, la existencia de error muestral en las muestras probabilísticas es irrelevante para el cálculo de estimadores, pues se entiende que las distintas características personales que pueden afectar la respuesta se cancelan entre ellos.

Lamentablemente, por temas de costos y de complejidad logística, ninguna de las encuestas electorales cuenta con este método. El más cercano es la encuesta CEP, pero incluye una etapa de estratificación y cuenta con una tasa de no respuesta sin reemplazo. Esta etapa es compleja pues hay segmentos de la población que son difíciles de encuestar, ya sea porque son inaccesibles (como personas de alto ingreso o personas en situación de calle) o porque prefieren no contestar (como jóvenes).

[La evidencia del Reino Unido](http://eprints.ncrm.ac.uk/3789/) post elección de 2015 mostró que las encuestas habían sido particularmente malas en llegar a encuestar votantes conservadores. Este tipo de errores se suelen corregir con ponderadores a partir del censo, pero los datos censales aún no han sido actualizados con posterioridad al pre censo de 2016 y también tienen límites respecto a lo que pueden hacer. Son útiles respecto a variables demográficas, pero no necesariamente respecto a preferencias políticas (o al menos eso parece).

La construcción de muestras es clave, pues aparte de la CEP, ninguna otra encuesta ocupa etapas probabilísticas. Esto quiere decir que confían de sobremanera en sus mecanismos de pre y post estratificación (en simple “hacer calza” la muestra con la población por métodos estadísticos) basados en los datos censales mencionados anteriormente. Claramente, algo puede estar fallando ahí.

La segunda fuente de error es el error de medición. Éste se refiere a cuando las preguntas que se hacen no logran capturar lo que realmente se quiere. Un clásico ejemplo es cuando le preguntamos a las personas si votaron o no en la elección pasada. Debido a una serie de sesgos de deseabilidad social, las personas tienden a decir qué votaron incluso si es que no lo han hecho. En ese caso, la pregunta no mide realmente el comportamiento de los encuestados.

Cuando se trata de preguntas sobre preferencias electorales, el error de medición se manifiesta, por ejemplo, a través de la presencia de espirales de silencio o de personas que prefieren no declarar sus preferencias, aunque éstas estén tomadas. Para lidiar con este aspecto, la encuesta CEP lleva años ocupando el método de “voto urna”, en el que el encuestado puede declarar su preferencia en una urna sin que lo vea el encuestador. Sin embargo, ese método no dio una estimación cercana al resultado de la elección.

Ambas opciones: problemas en el muestreo y en la medición, requieren de un análisis detallado y exhaustivo. Es importante que se vuelvan a revisar las bases de datos existentes en cuanto se liberen los nuevos datos censales, para saber si los ponderadores eran correctos o no. Además, hace falta análisis académico sobre error de medición, idealmente estudiando distintas fórmulas a través de experimentos.

### Votante probable

Se hizo bastante publicidad a los métodos de votante probable usados por las encuestadoras. En un conteo simple, hubo al menos 4 empresas o instituciones que ocuparon modelos similares para estimar la participación (Cadem, CEP, Criteria Research). Todos ocupaban una variación del mismo cóctel: interés en política, participación en elecciones en el pasado y la declaración de qué tan probable es que fueran a votar. Sólo la CEP (al menos en mi conocimiento) agregó datos demográficos de los votantes de las elecciones del 2013. Asimismo, todas las encuestadoras dieron un número entre 45% y 48%, lo que es bastante cercano a la realidad.

Ahora, hay varios potenciales focos de problema en este proceso. Por una parte, el que las empresas lleguen a un porcentaje similar al de votantes reales no asegura en ningún caso que dentro de ese porcentaje de encuestados se encuentren personas similares a los votantes. Por ejemplo, las preguntas ocupadas para generar la probabilidad de voto tienen un sesgo claro: minimizan a los jóvenes. Por lo tanto, se vuelve irrelevante cualquier cálculo de votante probable si éste es incapaz de anticipar quienes son esos potenciales votantes y si se parecen a los verdaderos votantes.

Para reflejar este punto, hice un pequeño ejercicio basado en la encuesta realizada con menor tiempo antes de la elección, la [Cadem Plaza Pública Número 201](http://plazapublica.cl/wp-content/uploads/Track-PP-201-NovS3-VF.pdf). Esta encuesta tuvo su campo en el martes, miércoles y jueves antes de la elección. En la tabla más abajo pongo las estimaciones del total de la muestra, eliminando a los indecisos (llevando los otros a base 100), las estimaciones de votante probable, el resultado final y las diferencias entre cada estimación.

<table width="702">
  <tr>
    <td width="87">
    </td>
    
    <td width="100">
      <strong>Total muestra sin indecisos</strong>
    </td>
    
    <td width="73">
      <strong>Votante Probable</strong>
    </td>
    
    <td width="79">
      <strong>Resultado elección</strong>
    </td>
    
    <td width="106">
      <strong>Diferencia votante probable – resultado</strong>
    </td>
    
    <td width="94">
      <strong>Diferencia total muestra – resultado</strong>
    </td>
  </tr>
  
  <tr>
    <td width="87">
      <strong>Piñera</strong>
    </td>
    
    <td width="100">
      38.96
    </td>
    
    <td width="73">
      40
    </td>
    
    <td width="79">
      36.64
    </td>
    
    <td width="106">
      3.36
    </td>
    
    <td width="94">
      2.32
    </td>
  </tr>
  
  <tr>
    <td width="87">
      <strong>Guillier</strong>
    </td>
    
    <td width="100">
      20.78
    </td>
    
    <td width="73">
      21
    </td>
    
    <td width="79">
      22.7
    </td>
    
    <td width="106">
      -1.7
    </td>
    
    <td width="94">
      -1.92
    </td>
  </tr>
  
  <tr>
    <td width="87">
      <strong>Sánchez</strong>
    </td>
    
    <td width="100">
      16.88
    </td>
    
    <td width="73">
      13
    </td>
    
    <td width="79">
      20.27
    </td>
    
    <td width="106">
      -7.27
    </td>
    
    <td width="94">
      -3.39
    </td>
  </tr>
  
  <tr>
    <td width="87">
      <strong>Goic</strong>
    </td>
    
    <td width="100">
      5.19
    </td>
    
    <td width="73">
      6
    </td>
    
    <td width="79">
      5.88
    </td>
    
    <td width="106">
      0.12
    </td>
    
    <td width="94">
      -0.69
    </td>
  </tr>
  
  <tr>
    <td width="87">
      <strong>Kast</strong>
    </td>
    
    <td width="100">
      6.49
    </td>
    
    <td width="73">
      6
    </td>
    
    <td width="79">
      7.93
    </td>
    
    <td width="106">
      -1.93
    </td>
    
    <td width="94">
      -1.44
    </td>
  </tr>
  
  <tr>
    <td width="87">
      <strong>MEO</strong>
    </td>
    
    <td width="100">
      7.79
    </td>
    
    <td width="73">
      5
    </td>
    
    <td width="79">
      5.71
    </td>
    
    <td width="106">
      -0.71
    </td>
    
    <td width="94">
      2.08
    </td>
  </tr>
  
  <tr>
    <td width="87">
      <strong>Navarro</strong>
    </td>
    
    <td width="100">
      0.65
    </td>
    
    <td width="73">
      0.5
    </td>
    
    <td width="79">
      0.36
    </td>
    
    <td width="106">
      0.14
    </td>
    
    <td width="94">
      0.29
    </td>
  </tr>
  
  <tr>
    <td width="87">
      <strong>Artés</strong>
    </td>
    
    <td width="100">
      0.65
    </td>
    
    <td width="73">
      0.5
    </td>
    
    <td width="79">
      0.51
    </td>
    
    <td width="106">
      -0.01
    </td>
    
    <td width="94">
      0.14
    </td>
  </tr>
  
  <tr>
    <td width="87">
      <strong>Indecisos</strong>
    </td>
    
    <td width="100">
    </td>
    
    <td width="73">
      8
    </td>
    
    <td width="79">
    </td>
    
    <td width="106">
    </td>
    
    <td width="94">
    </td>
  </tr>
</table>

La tabla muestra con claridad que, de haberse evitado el uso de votante probable, la estimación habría sido bastante más cercana a la realidad. Si bien hay algunos casos donde el error aumenta marginalmente al usar la muestra total (Guillier y MEO), en general el error se reduce significativamente. Sánchez, por ejemplo, esta mucho menos subrrepresentada en esta estimación. Una [métrica clásica][2] para medir la puntería de una encuesta consiste en el error absoluto promedio. En este indicador, el votante probable entrega un error promedio de 1,9 puntos, mientras que el error se reduce a 1,5 al mirar la muestra total.

Si, tal como dije anteriormente, el grupo que suele estar subrrepresentado en el votante probable son los más jóvenes, entonces la disminución del error en la muestra total es un indicio que apoya esta hipótesis. Esto no quiere decir que basta con eliminar el votante probable, sino que este es un punto de partida. Además, la inclusión de jóvenes puede explicar de mejor forma la subestimación de Beatriz Sánchez, pero no necesariamente la de José Antonio Kast.

### **Conclusiones y sugerencias de pasos a seguir**

Lo primero es consignar lo obvio: muchas cosas fallaron. Quizás lo más complicado para los encuestadores y para los académicos que utilizamos encuestas para nuestro trabajo es asumir que no existe una solución simple al problema. Desde el punto de vista académico esto es un desafío interesante, pero entiendo que la posición puede ser algo más incómoda para quienes están a cargo de la realización de los sondeos.

Lo segundo es que la solución no puede venir sólo desde las encuestadoras. En países donde se enfrentan desafíos similares, como EE.UU. y el Reino Unido, los organismos de administración electoral (como el SERVEL) han colaborado permitiendo el acceso a sus bases de datos. Esto es vital en el caso chileno. Es urgente que se realice un ejercicio de validación de voto, donde se sepa cuáles son las características demográficas de los votantes al nivel más desagregado posible. Sólo a partir de ahí será posible afinar los modelos de votante probable. Asimismo, la academia tiene un rol que cumplir en este proceso. Hay universidades con una larga experiencia en encuestas que podrían asumir la tarea de liderar este proceso.

También creo que necesitamos más encuestas. Esto puede sonar un poco irracional a la luz de lo ocurrido, pero soy un convencido que el proceso se mejora mientras hay más actores y más competencia. En el pasado he sido crítico de la metodología ocupada por encuestadoras como Criteria Research (panel online con post-estratificación), que tuvieron resultados mejores que las encuestadoras clásicas. En principio mantengo mis críticas y me inclino a pensar que su relativo éxito fue más bien azaroso, pero estoy dispuesto a estar equivocado (y, de hecho, lo agradecería).

Por último, me gustaría hacerme cargo de la acusación que hizo Beatriz Sánchez en su discurso la noche de la elección. Ella dijo que, si las encuestas hubieran reflejado mejor la realidad, quizás más gente hubiera votado por ella. La verdad es que ese es un contrafactual imposible de comprobar y, además, la evidencia es poco concluyente a la hora de mostrar un efecto directo entre encuestas y opción de voto. Sin embargo, donde sí afectan las encuestas es en el nivel de donaciones, en el monto de los créditos bancarios y en la moral de los equipos. Quizás Sánchez tiene un punto. Si las encuestas no la hubieran subestimado de forma sistemática durante los últimos meses, podría haber tenido una campaña más eficiente y mejor financiada. Si esto se hubiera traducido a votos o no permanecerá un misterio.

 [1]: http://www.duna.cl/columnistas/2017/11/23/por-que-fallaron-las-encuestas-por-javier-sajuria/
 [2]: https://www.statslife.org.uk/social-sciences/2573-cathie-marsh-lecture