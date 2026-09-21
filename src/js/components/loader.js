export function showLoader() {
  return new Promise((resolve) => {
    const loader = document.createElement("div");

    loader.id = "page-loader";

    loader.innerHTML = `

        <div class="
        fixed inset-0 z-50
        flex items-center
        justify-center
        bg-[#071a38]/90
        backdrop-blur">

            <div class="
            h-12 w-12
            animate-spin
            rounded-full
            border-4
            border-white/30
            border-t-blue-500">
            </div>

        </div>

        `;

    document.body.appendChild(loader);

    setTimeout(() => {
      resolve();
    }, 2000);
  });
}
