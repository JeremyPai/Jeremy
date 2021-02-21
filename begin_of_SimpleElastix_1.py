import SimpleITK as sitk

resultImage = sitk.Elastix(sitk.ReadImage("fixedImage.nii"), sitk.ReadImage("movingImage.nii"), "translation")

print("First time uploading the code to Github!")