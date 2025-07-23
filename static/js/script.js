
document.getElementById('btnCadastrar').addEventListener('click', function () {
    const form = document.getElementById('formMeta');
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
});

document.getElementById('btnVerMetas').addEventListener('click', function () {
    const form = document.getElementById('tableMetas');
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
});

document.getElementById('btnNovaDespesa').addEventListener('click', function () {
    const form = document.getElementById('formDespesa');
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
});

document.getElementById('btnNovaReceita').addEventListener('click', function () {
    const form = document.getElementById('formReceita');
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
});




function abrirModalD() {
  document.getElementById('modalD').style.display = 'flex';
}

function fecharModalD() {
  document.getElementById('modalD').style.display = 'none';
}

function abrirModalR() {
  document.getElementById('modalR').style.display = 'flex';
}

function fecharModalR() {
  document.getElementById('modalR').style.display = 'none';
}