<%inherit file="/basedesign.mako" />
<h1>Enter Object description</h1> <br/> <br/>

    ${h.form('email', method='post')}
    
    Author: ${h.text('author')} <br/>
    Email Address: ${h.text('email')} <br/>
    Name of Object: ${h.text('name')} <br/>
    Description: ${h.textarea('description')} <br/>
    Format: ${h.select('format','',[('format 1','format 1'),('format 2','format 2')])} <br/>
     
    Object: ${h.text('object')} <br/>
    Keywords: ${h.text('tags')} <br/>



   ${h.submit('submit','Submit Object')}
   ${h.end_form()}

