/* eslint-disable prettier/prettier */
"use server";


export const handleSubmit = async ( form_data: FormData) => {
    console.log("SERVER SIDE");
    console.log(form_data);

    const formulario = {
        user_id : "",
        conversar_id : "",
        pergunta : form_data.get("pergunta")
    };

    const API_URL: string|undefined = process.env.URL_BE;
    // const API_URL: string|undefined = "http://localhost:8091/teste";
    console.log(API_URL);

    // URL_BE=be_mpes
    if ( API_URL === undefined){
        // console.log('URL NÃO DEFINIDA');
        return "url não definida!";
    }

    const res = await fetch( API_URL, {
        method: 'POST',
        headers: {
            "Access-Control-Allow-Origin" : "*",
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods" : "GET,POST,PUT,DELETE,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With",
            "x-forwarded-host": "localhost:8091",
        },
        body: JSON.stringify(formulario)
    });
    
    if (res.ok) {
        const textoResposta = await res.text();
        // Lógica para quando o envio for bem-sucedido
        console.log('Formulário enviado com sucesso!');
        console.log( textoResposta );

        // return textoResposta;
        return textoResposta;
        
    } else {
        // Lógica para quando houver um erro
        console.error('Erro ao enviar o formulário');
        return "Nao voutou nada";
        // return "Nao voutou nada";
    }
    return "Nao voutou nada";
};

