## Directions
Create a folder called 'weights' inside the v2 directory
Inside the weights folder add a .pt file called 'best.pt'

## Sample curl request
curl --location 'http://127.0.0.1:5000/malai_upload' \
--form 'file=@"/C:/Users/pkase/Downloads/official-flames-logo-fire-circle-red-and-orange-011726586194.png"'

## Expected response
{
    "original_image": "http://127.0.0.1:5000/malai_upload/uploads\\official-flames-logo-fire-circle-red-and-orange-011726586194.png",
    "rotated_image": "http://127.0.0.1:5000/malai_upload/analyzed/analyzed_official-flames-logo-fire-circle-red-and-orange-011726586194.png",
    "time_taken": 23.139803886413574
}