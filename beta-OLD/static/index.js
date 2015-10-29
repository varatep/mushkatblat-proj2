var upload = function() {
    // var myFormData = new FormData();
    // myFormData.append('img', document.getElementById('file').files[0]);

    // $.ajax({
    //   url: 'http://localhost:1337/upload',
    //   type: 'POST',
    //   processData: false, // important
    //   contentType: false, // important
    //   dataType : 'json',
    //   data: myFormData
    // });
    //

    var reader = new FileReader();
    var line_data = $('#file').get(0);

    if (line_data.files.length) {
        var input_file = line_data.files[0];
        reader.readAsText(input_file);
        $(reader).on('load', function(e){
            data_line = e.target.result;
            $.ajax({
                    url:'http://localhost:1337/upload',
                    type:'POST',
                    data:{file: data_line},
                    success:function(returned_data){console.log(returned_data);},
                    error:function(){console.log('sorry...');}
            });

        });
    }
};