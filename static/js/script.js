
document.getElementById('btnCadastrar').addEventListener('click', function () {
    const form = document.getElementById('formMeta');
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
});

document.getElementById('btnVerMetas').addEventListener('click', function () {
    const form = document.getElementById('tableMetas');
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
});
