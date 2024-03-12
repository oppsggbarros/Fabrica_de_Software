<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <h1>Poggers</h1>
    <?php $nota = [];
    $nota[1] = 7;
    $nota[2] = 6;
    $nota[3] = 7;
    $nota[4] = 6;
    echo "A nota 1 é = $nota[1] <br>";
    echo "A nota 2 é = $nota[2] <br>";
    echo "A nota 3 é = $nota[3] <br>";
    $media = ($nota[1] + $nota[2] + $nota[3] + $nota[4]) / 4;
    echo "A media é " . $media . "<br>";
    $situacao = $media >= 6 ? "Aprovado" : "Reprovado";
    echo "Situação: " . $situacao . "<br>";
    ?>


    <?php

    function Exercice1($numero1, $numero2, $numero3)
    {

        $soma = $numero1 + $numero2 + $numero3;

        $media = $soma / 3;

        return $media;
    }

    $primeiroNumero = 5;
    $segundoNumero = 3;
    $terceiroNumero = 10;

    $mediaFinal = Exercice1($primeiroNumero, $segundoNumero, $terceiroNumero);

    echo "O media final é: " . $mediaFinal . "<br>";
    ?>


    <?php

    function calcularPorcentagem($valor)
    {

        $porcentagem = $valor * 0.05;
        $porcentagem2 = $valor * 0.50;


        echo "50% de $valor é: $porcentagem <br>";
        echo "5% de $valor é : $porcentagem2 <br>";
    }


    $valorInformado = 15621;

    calcularPorcentagem($valorInformado);
    ?>


    <?php
    function calcularosQuadrados($number1, $number2)
    {
        $soma = $number1 ** 2 + $number2 ** 2;

        echo "soma dos quadrados dos números é $soma <br>";
    }
    $quadrado1 = 5;
    $quadrado2 = 4;
    calcularosQuadrados($quadrado1, $quadrado2);
    ?>


    <?php
    
    function calcularIMCHomem($altura, $peso)
    {
        $imc = $peso / ($altura * $altura);
        return $imc;
    }

    
    function calcularIMCMulher($altura, $peso)
    {
        $imc = $peso / ($altura * $altura);
        return $imc;
    }

    
    function exibirResultadoIMC($imc, $sexo)
    {
        echo "O IMC para $sexo é: $imc\n";
        echo "Classificação: ";
        if ($imc < 18.5) {
            echo "Abaixo do peso";
        } elseif ($imc >= 18.5 && $imc < 24.9) {
            echo "Peso normal";
        } elseif ($imc >= 25 && $imc < 29.9) {
            echo "Sobrepeso";
        } elseif ($imc >= 30 && $imc < 34.9) {
            echo "Obesidade grau I";
        } elseif ($imc >= 35 && $imc < 39.9) {
            echo "Obesidade grau II";
        } else {
            echo "Obesidade grau III";
        }
    }

    
    $altura = 1.75; 
    $peso = 70; 
    $sexo = 'mulhe'; 

    if ($sexo == 'homem') {
        $imc = calcularIMCHomem($altura, $peso);
        exibirResultadoIMC($imc, $sexo);
    } elseif ($sexo == 'mulhe') {
        $imc = calcularIMCMulher($altura, $peso);
        exibirResultadoIMC($imc, $sexo);
    } else {
        echo "Sexo não reconhecido.";
    }
    ?>


</body>

</html>