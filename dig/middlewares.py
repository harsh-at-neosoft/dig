from django.http import HttpResponse
from dig.settings import BASE_DIR
from utilities.constants import constants


class ServeStaticFiles(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        # This runs only at the start of the server #
    
    def __call__(self,request,*args,**kwargs):             

        ## single page website static-file-server ##

        # Validate method     
        if request.method == "GET":                

            # Validate Allowed Files     
            requested_file = request.path.split("/")[1] if request.path else ""
            if not requested_file:
                requested_file="index.html"    
            allowedFiles = constants["AllowedStaticFiles"]

            if (requested_file in allowedFiles):                              
                # Set the content-type according to requested file
                requested_file_extension = requested_file.split(".")[1] if requested_file else "html"

                content_type = f'text/{("javascript" if requested_file_extension == "js" else requested_file_extension)}'

                # Get file contents > Send them in response    
                file_to_serve=""
                
                with open(f'{BASE_DIR}/client/{requested_file}') as file:
                    for line in file:            
                            file_to_serve+=line                                
                
                return HttpResponse(file_to_serve,content_type=content_type,headers={'customHead':"I am a custom head"})                                                 
                        
            # Pass the request to other middlewares/views if not serving static files
            response = self.get_response(request)
            # Code here to modify response before returning to the client            
            return response
    