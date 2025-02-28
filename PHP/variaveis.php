<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Variaveis PHP</title>
</head>
<body>
    <h1>Testando PHP</h1>
    <?php
        $idade = 3;
        $salario = 1825.54;
        $nome = "Leonardo";
        $casado = false; 

        $idade = (int) 18; //forcando a tipagem
        $nome = (string) "Caroline" 

        //echo $nome. " tem ". $idade. " anos!";
        echo "$nome tem $idade anos!";
    ?>
</body>
</html>