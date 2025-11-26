export function resizeImage(file: File, maxSize : number = 75): Promise<Blob> {
    return new Promise((resolve, reject) => {
        const img = new Image();
        const reader = new FileReader();

        reader.onload = (e) => {
            if (!e.target?.result) {
                return reject("Failed to read file")
            }

            img.src = e.target.result as string;
        }

        img.onload = () => {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            if (!ctx) {
                return reject("No canvas context");
            }

            const ogWidth = img.width;
            const ogHeight = img.height;

            const scale = Math.min(
                maxSize / ogHeight,
                maxSize / ogWidth
            );

            const newWidth = ogWidth * scale;
            const newHeight = ogHeight * scale;

            canvas.width = newWidth;
            canvas.height = newHeight;

            ctx.drawImage(img, 0, 0, newWidth, newHeight);

            canvas.toBlob(
                (blob) => {
                    if (!blob) {
                        return reject("Failed to create blob");
                    }
                    resolve(blob);
                },
                "image/jpeg", 0.9
            )

        }

        reader.readAsDataURL(file);
    })
}