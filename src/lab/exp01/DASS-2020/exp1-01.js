var wavesurfer = WaveSurfer.create({
                container: '#waveform',
                waveColor: 'blue',
                barHeight: 2,
                barGap: 1,
                height: 500,
                backgroundColor: 'grey',
            });


function playButton(){
    wavesurfer.playPause();
}

function LoadExperiment(item){
   loadExpFrame(item.value);
}

function hideDiv(){
    document.getElementById('SelectLoad').style.visibility = 'hidden';
}

var content1,content2,content3,content4;
var content1syl,content1phn,content1wrd;
var content2syl,content2phn,content2wrd;
var content3syl,content3phn,content3wrd;
var content1sy4,content4phn,content4wrd;

function preload(){
    content1 = loadStrings("wav/ex1.txt");
    content2 = loadStrings("wav/ex2.txt");
    content3 = loadStrings("wav/ex3.txt");
    content4 = loadStrings("wav/ex4.txt");
    content1syl = loadStrings("wav/ex1.syl");
    content2syl = loadStrings("wav/ex2.syl");
    content3syl = loadStrings("wav/ex3.syl");
    content4syl = loadStrings("wav/ex4.syl");
    content1phn = loadStrings("wav/ex1.phn");
    content2phn = loadStrings("wav/ex2.phn");
    content3phn = loadStrings("wav/ex3.phn");
    content4phn = loadStrings("wav/ex4.phn");
    content1wrd = loadStrings("wav/ex1.wrd");
    content2wrd = loadStrings("wav/ex2.wrd");
    content3wrd = loadStrings("wav/ex3.wrd");
    content4wrd = loadStrings("wav/ex4.wrd");
}

function setup() {
    noCanvas();
    //console.log(content1phn);
}

function loadExpFrame(expnum=0) {
    if(expnum != 0){
        document.getElementById('swunit').selectedIndex = 0;
        document.getElementById('SelectLoad').style.visibility = 'visible';
        document.getElementById("lang").value = expnum;
        addplaybacks('syll');
        if(expnum == 1){
            wavesurfer.load('wav/ex1.wav');
            document.getElementById("utterance").innerHTML = content1[0];
            document.getElementById("transliteration").innerHTML = content1[1];
            document.getElementById("subword").innerHTML = content1[2];
        }
        
        if(expnum == 2){
            wavesurfer.load('wav/ex2.wav');
            document.getElementById("utterance").innerHTML = content2[0];
            document.getElementById("transliteration").innerHTML = content2[1];
            document.getElementById("subword").innerHTML = content2[2];
        }
        
        if(expnum == 3){
            wavesurfer.load('wav/ex3.wav');
            document.getElementById("utterance").innerHTML = content3[0];
            document.getElementById("transliteration").innerHTML = content3[1];
            document.getElementById("subword").innerHTML = content3[2];
        }
        
        if(expnum == 4){
            wavesurfer.load('wav/ex4.wav');
            document.getElementById("utterance").innerHTML = content4[0];
            document.getElementById("transliteration").innerHTML = content4[1];
            document.getElementById("subword").innerHTML = content4[2];
        }
        
    }
    if(expnum == 0){
        document.getElementById('SelectLoad').style.visibility = 'hidden';
    }
}

function loadSubword(subword) {
        var field = document.getElementById("lang").value;
        addplaybacks(subword.value);
        if(subword.value == 'syll'){
            if(field == 1){
                document.getElementById("subword").innerHTML = content1[2];
            }
            
            if(field == 2){
                document.getElementById("subword").innerHTML = content2[2];
            }
            
            if(field == 3){
                document.getElementById("subword").innerHTML = content3[2];
            }
            
            if(field == 4){
                document.getElementById("subword").innerHTML = content4[2];
            }
        }
    
        if(subword.value == 'phon'){
            
            if(field == 1){
                document.getElementById("subword").innerHTML = content1[3];
            }
            
            if(field == 2){
                document.getElementById("subword").innerHTML = content2[3];
            }
            
            if(field == 3){
                document.getElementById("subword").innerHTML = content3[3];
            }
            
            if(field == 4){
                document.getElementById("subword").innerHTML = content4[3];
            }
            
        }
    
        if(subword.value == 'word'){
            if(field == 1){
                document.getElementById("subword").innerHTML = content1[1];
            }
            
            if(field == 2){
                document.getElementById("subword").innerHTML = content2[1];
            }
            
            if(field == 3){
                document.getElementById("subword").innerHTML = content3[1];
            }
            
            if(field == 4){
                document.getElementById("subword").innerHTML = content4[1];
            }
        }
}

function reset_table() {
    var table = document.getElementById("Subword");
    var rows = table.getElementsByTagName("tr");
    var lengt = rows.length;
    for(var i = 1;i < lengt;i++){
        table.deleteRow(1);
    }
}


function addplaybacks(subword){
    console.log(content1syl);
    var table = document.getElementById("Subword");
    var new_table = document.createElement('tbody');
    reset_table();
    var itr;
    
    if(subword == 'syll'){
        var field = document.getElementById("lang").value;
        if(field == 1){
            for(itr = 0;itr < content1syl.length-1;itr++){
                table.appendChild(tr = document.createElement("tr"));
                var fields = content1syl[itr].split(" ");
                console.log(fields);
                for(var i=0;i < 3;i++){
                    tr.appendChild(td = document.createElement("td"));
                    
                    if(i == 0){
                        var begin = 0.000066375*parseFloat(fields[1]);
                        var end = 0.000066375*parseFloat(fields[2]);
                        td.innerHTML = '<button type="button" style="width:120px;" onclick="wavesurfer.play('+begin+','+end+')">'+fields[0]+'</button>';
                    }
                    
                    else{
                        td.innerHTML = fields[i];
                    }
                }
            }
        }
        
        if(field == 2){
            for(itr = 0;itr < content2syl.length-1;itr++){
                table.appendChild(tr = document.createElement("tr"));
                var fields = content2syl[itr].split(" ");
                console.log(fields);
                for(var i=0;i < 3;i++){
                    tr.appendChild(td = document.createElement("td"));
                    
                    if(i == 0){
                        var begin = 0.000066375*parseFloat(fields[1]);
                        var end = 0.000066375*parseFloat(fields[2]);
                        td.innerHTML = '<button type="button" style="width:120px;" onclick="wavesurfer.play('+begin+','+end+')">'+fields[0]+'</button>';
                    }
                    
                    else{
                        td.innerHTML = fields[i];
                    }
                }
                
            }
        }
        
        if(field == 3){
            for(itr = 0;itr < content3syl.length-1;itr++){
                table.appendChild(tr = document.createElement("tr"));
                var fields = content3syl[itr].split(" ");
                console.log(fields);
                for(var i=0;i < 3;i++){
                    tr.appendChild(td = document.createElement("td"));
                    
                    if(i == 0){
                        var begin = 0.000066375*parseFloat(fields[1]);
                        var end = 0.000066375*parseFloat(fields[2]);
                        td.innerHTML = '<button type="button" style="width:120px;" onclick="wavesurfer.play('+begin+','+end+')">'+fields[0]+'</button>';
                    }
                    
                    else{
                        td.innerHTML = fields[i];
                    }
                }
            }
        }
        
        if(field == 4){
            for(itr = 0;itr < content4syl.length-1;itr++){
                table.appendChild(tr = document.createElement("tr"));
                var fields = content4syl[itr].split(" ");
                console.log(fields);
                for(var i=0;i < 3;i++){
                    tr.appendChild(td = document.createElement("td"));
                    
                    if(i == 0){
                        var begin = 0.000066375*parseFloat(fields[1]);
                        var end = 0.000066375*parseFloat(fields[2]);
                        td.innerHTML = '<button type="button" style="width:120px;" onclick="wavesurfer.play('+begin+','+end+')">'+fields[0]+'</button>';
                    }
                    
                    else{
                        td.innerHTML = fields[i];
                    }
                }
            }
        }
    }
    
    if(subword == 'phon'){
        console.log("I got");
        var field = document.getElementById("lang").value;
        if(field == 1){
            for(itr = 0;itr < content1phn.length-1;itr++){
                table.appendChild(tr = document.createElement("tr"));
                var fields = content1phn[itr].split(" ");
                console.log(fields);
                for(var i=0;i < 3;i++){
                    tr.appendChild(td = document.createElement("td"));
                    
                    if(i == 0){
                        var begin = 0.000066375*parseFloat(fields[1]);
                        var end = 0.000066375*parseFloat(fields[2]);
                        td.innerHTML = '<button type="button" style="width:120px;" onclick="wavesurfer.play('+begin+','+end+')">'+fields[0]+'</button>';
                    }
                    
                    else{
                        td.innerHTML = fields[i];
                    }
                }
            }
        }
        
        if(field == 2){
            for(itr = 0;itr < content2phn.length-1;itr++){
                
                table.appendChild(tr = document.createElement("tr"));
                var fields = content2phn[itr].split(" ");
                console.log(fields);
                for(var i=0;i < 3;i++){
                    tr.appendChild(td = document.createElement("td"));
                    
                    if(i == 0){
                        var begin = 0.000066375*parseFloat(fields[1]);
                        var end = 0.000066375*parseFloat(fields[2]);
                        td.innerHTML = '<button type="button" style="width:120px;" onclick="wavesurfer.play('+begin+','+end+')">'+fields[0]+'</button>';
                    }
                    
                    else{
                        td.innerHTML = fields[i];
                    }
                }
                
            }
        }
        
        if(field == 3){
            for(itr = 0;itr < content3phn.length-1;itr++){
                
                table.appendChild(tr = document.createElement("tr"));
                var fields = content3phn[itr].split(" ");
                console.log(fields);
                for(var i=0;i < 3;i++){
                    tr.appendChild(td = document.createElement("td"));
                    
                    if(i == 0){
                        var begin = 0.000066375*parseFloat(fields[1]);
                        var end = 0.000066375*parseFloat(fields[2]);
                        td.innerHTML = '<button type="button" style="width:120px;" onclick="wavesurfer.play('+begin+','+end+')">'+fields[0]+'</button>';
                    }
                    
                    else{
                        td.innerHTML = fields[i];
                    }
                }
                
            }
        }
        
        if(field == 4){
            for(itr = 0;itr < content4phn.length-1;itr++){
                table.appendChild(tr = document.createElement("tr"));
                var fields = content4phn[itr].split(" ");
                console.log(fields);
                for(var i=0;i < 3;i++){
                    tr.appendChild(td = document.createElement("td"));
                    
                    if(i == 0){
                        var begin = 0.000066375*parseFloat(fields[1]);
                        var end = 0.000066375*parseFloat(fields[2]);
                        td.innerHTML = '<button type="button" style="width:120px;" onclick="wavesurfer.play('+begin+','+end+')">'+fields[0]+'</button>';
                    }
                    
                    else{
                        td.innerHTML = fields[i];
                    }
                }
                
            }
        }
    }
    
    if(subword == 'word'){
        var field = document.getElementById("lang").value;
        if(field == 1){
            for(itr = 0;itr < content1wrd.length-1;itr++){
                
                table.appendChild(tr = document.createElement("tr"));
                var fields = content1wrd[itr].split(" ");
                console.log(fields);
                for(var i=0;i < 3;i++){
                    tr.appendChild(td = document.createElement("td"));
                    
                    if(i == 0){
                        var begin = 0.000066375*parseFloat(fields[1]);
                        var end = 0.000066375*parseFloat(fields[2]);
                        td.innerHTML = '<button type="button" style="width:120px;" onclick="wavesurfer.play('+begin+','+end+')">'+fields[0]+'</button>';
                    }
                    
                    else{
                        td.innerHTML = fields[i];
                    }
                }
                
            }
        }
        
        if(field == 2){
            for(itr = 0;itr < content2wrd.length-1;itr++){
                
                table.appendChild(tr = document.createElement("tr"));
                var fields = content2wrd[itr].split(" ");
                console.log(fields);
                for(var i=0;i < 3;i++){
                    tr.appendChild(td = document.createElement("td"));
                    
                    if(i == 0){
                        var begin = 0.000066375*parseFloat(fields[1]);
                        var end = 0.000066375*parseFloat(fields[2]);
                        td.innerHTML = '<button type="button" style="width:120px;" onclick="wavesurfer.play('+begin+','+end+')">'+fields[0]+'</button>';
                    }
                    
                    else{
                        td.innerHTML = fields[i];
                    }
                }
                
            }
        }
        
        if(field == 3){
            for(itr = 0;itr < content3wrd.length-1;itr++){
                
                table.appendChild(tr = document.createElement("tr"));
                var fields = content3wrd[itr].split(" ");
                console.log(fields);
                for(var i=0;i < 3;i++){
                    tr.appendChild(td = document.createElement("td"));
                    
                    if(i == 0){
                        var begin = 0.000066375*parseFloat(fields[1]);
                        var end = 0.000066375*parseFloat(fields[2]);
                        td.innerHTML = '<button type="button" style="width:120px;" onclick="wavesurfer.play('+begin+','+end+')">'+fields[0]+'</button>';
                    }
                    
                    else{
                        td.innerHTML = fields[i];
                    }
                }
                
            }
        }
        
        if(field == 4){
            for(itr = 0;itr < content4wrd.length-1;itr++){
                
                table.appendChild(tr = document.createElement("tr"));
                var fields = content4wrd[itr].split(" ");
                console.log(fields);
                for(var i=0;i < 3;i++){
                    tr.appendChild(td = document.createElement("td"));
                    
                    if(i == 0){
                        var begin = 0.000066375*parseFloat(fields[1]);
                        var end = 0.000066375*parseFloat(fields[2]);
                        td.innerHTML = '<button type="button" style="width:120px;" onclick="wavesurfer.play('+begin+','+end+')">'+fields[0]+'</button>';
                    }
                    
                    else{
                        td.innerHTML = fields[i];
                    }
                }
                
            }
        }
    }
    
}


