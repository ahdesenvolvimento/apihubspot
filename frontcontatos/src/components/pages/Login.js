export default function Login(){
    return (
        <div className="text-center" style={{fontSize: '50px'}}>
            <a 
            target="_blank" 
            href="https://app.hubspot.com/oauth/authorize?client_id=1f354f0f-7797-423e-b7c7-be178f48d51f&redirect_uri=http://localhost:3000/&scope=crm.objects.contacts.read%20crm.objects.contacts.write%20crm.schemas.contacts.read%20crm.schemas.contacts.write">Para acessar a plataforma, você precisa clicar neste link.</a>
        </div>
    )
}