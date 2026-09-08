// Script interactivo para Taller Web
document.addEventListener('DOMContentLoaded', () => {
    const btnTestApi = document.getElementById('btnTestApi');
    const apiResultContainer = document.getElementById('apiResultContainer');
    const apiResultCode = document.getElementById('apiResultCode');
    const btnCloseApiResult = document.getElementById('btnCloseApiResult');

    if (btnTestApi && apiResultContainer && apiResultCode) {
        btnTestApi.addEventListener('click', async () => {
            btnTestApi.disabled = true;
            btnTestApi.innerHTML = '<span class="spinner-border spinner-border-sm me-1" role="status"></span> Consultando...';

            try {
                const response = await fetch('/api/info');
                if (!response.ok) {
                    throw new Error(HTTP  - );
                }
                const data = await response.json();
                apiResultCode.textContent = JSON.stringify(data, null, 2);
                apiResultContainer.classList.remove('d-none');
            } catch (error) {
                apiResultCode.textContent = Error al consultar la API: ;
                apiResultContainer.classList.remove('d-none');
            } finally {
                btnTestApi.disabled = false;
                btnTestApi.innerHTML = '<i class="bi bi-play-circle me-1"></i> Probar API en Vivo';
            }
        });

        if (btnCloseApiResult) {
            btnCloseApiResult.addEventListener('click', () => {
                apiResultContainer.classList.add('d-none');
            });
        }
    }
});

