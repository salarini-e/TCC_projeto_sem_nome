
// Obtenha a referência para o elemento Canvas
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

// Defina as propriedades das partículas
const gravity = 0.1;

const particle1 = {
    x: canvas.width / 2,  // Posição X da partícula 1
    y: canvas.height / 2, // Posição Y da partícula 1
    radius: 20,           // Raio da partícula 1
    speed: 0.03,          // Velocidade de rotação da partícula 1
    angle: 0,              // Ângulo inicial da partícula 1
    mass: 1
};

const particle2 = {
    x: canvas.width / 2,  // Posição X da partícula 2
    y: canvas.height / 2, // Posição Y da partícula 2
    radius: 10,           // Raio da partícula 2
    speed: 0.1,           // Velocidade de rotação da partícula 2
    angle: 0,              // Ângulo inicial da partícula 2
    mass: 2
};

function draw() {
    // Limpar o canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Calcular as novas posições das partículas
    // const dx1 = particle1.x - canvas.width / 2;
    // const dy1 = particle1.y - canvas.height / 2;
    // const distance1 = Math.sqrt(dx1 * dx1 + dy1 * dy1);
    // const gravity1 = gravity / (distance1 * distance1);
    // particle1.angle += particle1.speed + gravity1;

    // const dx2 = particle2.x - particle1.x;
    // const dy2 = particle2.y - particle1.y;
    // const distance2 = Math.sqrt(dx2 * dx2 + dy2 * dy2);
    // const gravity2 = gravity / (distance2 * distance2);
    // particle2.angle += particle2.speed + gravity2;
    
    // Calcular as novas posições das partículas
    particle1.x = canvas.width / 2 + Math.cos(particle1.angle) * 100;
    particle1.y = canvas.height / 2 + Math.sin(particle1.angle) * 100;

    particle2.x = particle1.x + Math.cos(particle2.angle) * 50;
    particle2.y = particle1.y + Math.sin(particle2.angle) * 50;

    // Desenhar as partículas
    ctx.beginPath();
    ctx.arc(particle1.x, particle1.y, particle1.radius, 0, Math.PI * 2);
    ctx.fillStyle = "blue";
    ctx.fill();

    ctx.beginPath();
    ctx.arc(particle2.x, particle2.y, particle2.radius, 0, Math.PI * 2);
    ctx.fillStyle = "red";
    ctx.fill();

    // Atualizar os ângulos das partículas para a próxima iteração
    particle1.angle += particle1.speed;
    particle2.angle += particle2.speed;

    // Repetir a animação
    requestAnimationFrame(draw);
}

// Iniciar a animação
draw();


