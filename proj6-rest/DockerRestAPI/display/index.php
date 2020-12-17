<html>
    <head>
        <title>CIS 322 REST-api demo: Brevets list</title>
    </head>

    <body>
        <h1>List of All</h1>
        <ul>
            <?php
            $ajson = file_get_contents('http://laptop-service/listAll');
            $aobj = json_decode($ajson);
              $adatas = $aobj->data;
            foreach ($adatas as $d) {
                echo "<li>$d[0]\t$d[1]\t$d[2]\t$d[3]\t$d[4]</li>";
            }
            echo "\nJSON";
            $json = file_get_contents('http://laptop-service/listAll/json');
            $obj = json_decode($json);
              $datas = $obj->data;
            foreach ($datas as $d) {
                echo "<li>$d[0]\t$d[1]\t$d[2]\t$d[3]\t$d[4]</li>";
            }
            ?>
        </ul>
        <h1>List of Open</h1>
        <ul>
            <?php
            $ojson = file_get_contents('http://laptop-service/listOpenOnly');
            $oobj = json_decode($ojson);
              $odatas = $oobj->data;
            foreach ($odatas as $d) {
                echo "<li>$d[0]\t$d[1]\t$d[2]\t$d[3]</li>";
            }
            echo "\nJSON";
            $json = file_get_contents('http://laptop-service/listOpenOnly/json');
            $obj = json_decode($json);
              $datas = $obj->data;
            foreach ($datas as $d) {
                echo "<li>$d[0]\t$d[1]\t$d[2]\t$d[3]</li>";
            }
            ?>
        </ul>
        <h1>List of Close</h1>
        <ul>
            <?php
            $cjson = file_get_contents('http://laptop-service/listCloseOnly');
            $cobj = json_decode($cjson);
              $cdatas = $cobj->data;
            foreach ($cdatas as $d) {
                echo "<li>$d[0]\t$d[1]\t$d[2]\t$d[3]</li>";
            }
            echo "\nJSON";
            $json = file_get_contents('http://laptop-service/listCloseOnly/json');
            $obj = json_decode($json);
              $datas = $obj->data;
            foreach ($datas as $d) {
                echo "<li>$d[0]\t$d[1]\t$d[2]\t$d[3]</li>";
            }
            ?>
        </ul>
    </body>
    <body>
        <h1>List of All in csv</h1>
        <ul>
            <?php
            $csv = file_get_contents('http://laptop-service/listAll/csv');
            $rcsv = json_decode($csv);
            $rcsv = nl2br($rcsv);
            echo $rcsv;
        </ul>
        <h1>List of Open in csv</h1>
        <ul>
            <?php
            $csv = file_get_contents('http://laptop-service/listOpenOnly/csv');
            $ocsv = json_decode($csv);
            $ocsv = nl2br($ocsv);
            echo $ocsv;
            ?>
        </ul>
        <h1>List of Close in csv</h1>
        <ul>
            <?php
            $csv = file_get_contents('http://laptop-service/listCloseOnly/csv');
            $ccsv = json_decode($csv);
            $ccsv = nl2br($ccsv);
            echo $ccsv;
            ?>
        </ul>
    </body>
</html>