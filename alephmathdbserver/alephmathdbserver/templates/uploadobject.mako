<%inherit file="/basedesign.mako" />
<h1>Enter Object description</h1> <br/> <br/>
    ${h.form('submit_object_info', method='post')}
<!-- Accordion -->
		<h2 class="Headers">DAS</h2>
		<div id="accordion">
			<div>
				<h3><a href="#">Information about the submitter</a></h3>
				
    				<div> Author: <br/> ${h.text('author')} <br/>
                                 Email Address:  <br/> ${h.text('email')} </div>

			</div>
			<div>
				<h3><a href="#">Basic information about the object</a></h3>
				<div>Phasellus mattis tincidunt nibh.
    Name of Object:  <br/> ${h.text('name')} <br/>
    Description:  <br/> ${h.textarea('description')} <br/>
    Format:  <br/> ${h.select('format','',[('format 1','format 1'),('format 2','format 2')],class_='ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only')} <br/>
     
    Object:  <br/> ${h.text('object')} <br/></div>
			</div>
			<div>
				<h3><a href="#">Additional Information</a></h3>
				<div>Keywords:  <br/> ${h.text('tags')} <br/></div>
			</div>
		</div>
    


   ${h.submit('submit','Submit Object',class_="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only")}
   ${h.end_form()}

