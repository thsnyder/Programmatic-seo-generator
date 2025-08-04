import { useState } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Input } from '@/components/ui/input.jsx'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Textarea } from '@/components/ui/textarea.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { CopyButton } from '@/components/ui/copy-button.jsx'
import { Modal } from '@/components/ui/modal.jsx'
import { MarkdownPreview } from '@/components/ui/markdown-preview.jsx'
import { Select } from '@/components/ui/select.jsx'
import { Plus, FileText, Wand2, Loader2, Sparkles, Eye, Trash2, Download } from 'lucide-react'
import './App.css'

function App() {
  const [rows, setRows] = useState([
    { 
      id: 1, 
      keyword: '', 
      product: 'Files.com', 
      articleTitle: '', 
      fullArticle: '', 
      metaTitle: '', 
      metaDescription: '', 
      status: 'empty',
      isLoading: false
    }
  ])
  const [previewModal, setPreviewModal] = useState({ isOpen: false, content: '', title: '' })

  const productOptions = [
    { value: 'Files.com', label: 'Files.com' },
    { value: 'ExaVault', label: 'ExaVault' },
    { value: 'ExpanDrive', label: 'ExpanDrive' }
  ]

  const addRow = () => {
    const newRow = {
      id: Date.now(),
      keyword: '',
      product: 'Files.com',
      articleTitle: '',
      fullArticle: '',
      metaTitle: '',
      metaDescription: '',
      status: 'empty',
      isLoading: false
    }
    setRows([...rows, newRow])
  }

  const removeRow = (id) => {
    if (rows.length > 1) {
      setRows(rows.filter(row => row.id !== id))
    }
  }

  const updateKeyword = (id, keyword) => {
    setRows(rows.map(row => 
      row.id === id ? { 
        ...row, 
        keyword, 
        status: keyword ? 'ready' : 'empty',
        // Clear content when keyword changes
        articleTitle: '',
        fullArticle: '',
        metaTitle: '',
        metaDescription: ''
      } : row
    ))
  }

  const updateProduct = (id, product) => {
    setRows(rows.map(row => 
      row.id === id ? { 
        ...row, 
        product,
        // Clear content when product changes
        articleTitle: '',
        fullArticle: '',
        metaTitle: '',
        metaDescription: '',
        status: row.keyword ? 'ready' : 'empty'
      } : row
    ))
  }

  const generateContent = async (id) => {
    const row = rows.find(r => r.id === id)
    if (!row.keyword) return

    setRows(rows.map(r => 
      r.id === id ? { ...r, isLoading: true } : r
    ))
    
    try {
      const response = await fetch('/api/generate_content', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          keyword: row.keyword,
          product: row.product
        })
      })
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const data = await response.json()
      
      setRows(rows.map(r => 
        r.id === id ? { 
          ...r, 
          articleTitle: data.article_title,
          fullArticle: data.full_article,
          metaTitle: data.meta_title,
          metaDescription: data.meta_description,
          status: 'complete',
          isLoading: false
        } : r
      ))
    } catch (error) {
      console.error('Error generating content:', error)
      alert('Error generating content. Please make sure the backend server is running.')
      setRows(rows.map(r => 
        r.id === id ? { ...r, isLoading: false } : r
      ))
    }
  }

  const getStatusBadge = (status) => {
    const statusConfig = {
      'empty': { 
        label: 'Enter Keyword', 
        className: 'bg-files-light-gray text-white border-files-light-pink' 
      },
      'ready': { 
        label: 'Ready to Generate', 
        className: 'bg-files-light-pink text-files-primary-red border-files-super-light-red' 
      },
      'complete': { 
        label: 'Complete', 
        className: 'bg-files-super-light-red/30 text-files-super-dark-maroon border-files-bright-red' 
      }
    }
    
    const config = statusConfig[status] || statusConfig['empty']
    return <Badge className={config.className}>{config.label}</Badge>
  }

  const openPreview = (content, title) => {
    setPreviewModal({ isOpen: true, content, title })
  }

  const closePreview = () => {
    setPreviewModal({ isOpen: false, content: '', title: '' })
  }

  const copyPreviewContent = () => {
    navigator.clipboard.writeText(previewModal.content)
      .then(() => {
        console.log('Article content copied to clipboard')
      })
      .catch(err => {
        console.error('Failed to copy content: ', err)
      })
  }

  const exportAllContent = () => {
    const completedRows = rows.filter(row => row.status === 'complete')
    if (completedRows.length === 0) {
      alert('No completed content to export')
      return
    }

    let exportText = '# SEO Content Export\n\n'
    
    completedRows.forEach((row, index) => {
      exportText += `## ${index + 1}. ${row.keyword}\n\n`
      exportText += `**Product:** ${row.product}\n\n`
      exportText += `**Article Title:** ${row.articleTitle}\n\n`
      exportText += `**Meta Title:** ${row.metaTitle}\n\n`
      exportText += `**Meta Description:** ${row.metaDescription}\n\n`
      exportText += `**Full Article:**\n\n${row.fullArticle}\n\n`
      exportText += '---\n\n'
    })

    const blob = new Blob([exportText], { type: 'text/markdown' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = 'seo-content-export.md'
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-files-light-gray via-files-light-pink to-files-super-light-red p-4 lg:p-8">
      <div className="max-w-7xl mx-auto space-y-6">
        {/* Header */}
        <div className="text-center space-y-4">
          <div className="flex items-center justify-center gap-3">
            <div className="p-3 bg-gradient-to-r from-files-primary-red to-files-bright-red rounded-xl shadow-lg">
              <Sparkles className="h-8 w-8 text-white" />
            </div>
            <h1 className="text-3xl lg:text-4xl font-bold bg-gradient-to-r from-files-primary-red to-files-bright-red bg-clip-text text-transparent">
              SEO Content Generator
            </h1>
          </div>
          <p className="text-base lg:text-lg text-files-headline-black/70 max-w-2xl mx-auto leading-relaxed">
            Generate complete SEO content in one click. Enter keywords and get full articles with titles, meta descriptions, and more.
          </p>
        </div>

        {/* Controls */}
        <div className="flex flex-col sm:flex-row gap-4 justify-between items-start sm:items-center">
          <div className="flex gap-2">
            <Button 
              onClick={addRow} 
              className="bg-gradient-to-r from-files-primary-red to-files-bright-red hover:from-files-maroon hover:to-files-primary-red text-white shadow-lg hover:shadow-xl transition-all duration-200 flex items-center gap-2"
            >
              <Plus className="h-4 w-4" />
              Add Row
            </Button>
            <Button 
              onClick={exportAllContent}
              variant="outline"
              className="border-files-light-pink text-files-primary-red hover:bg-files-light-pink transition-all duration-200 flex items-center gap-2"
            >
              <Download className="h-4 w-4" />
              Export All
            </Button>
          </div>
          <div className="text-sm text-files-headline-black/60">
            {rows.filter(r => r.status === 'complete').length} of {rows.length} completed
          </div>
        </div>

        {/* Content Cards */}
        <div className="grid gap-6">
          {rows.map((row) => (
            <Card key={row.id} className="shadow-lg border-0 bg-white/80 backdrop-blur-sm">
              <CardHeader className="border-b border-files-light-pink bg-gradient-to-r from-files-light-gray to-files-light-pink/30">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-4">
                    <CardTitle className="text-lg font-semibold text-files-headline-black flex items-center gap-2">
                      <FileText className="h-5 w-5 text-files-primary-red" />
                      Content Row {row.id}
                    </CardTitle>
                    {getStatusBadge(row.status)}
                  </div>
                  {rows.length > 1 && (
                    <Button
                      onClick={() => removeRow(row.id)}
                      variant="ghost"
                      size="sm"
                      className="text-files-bright-red hover:text-files-maroon hover:bg-files-light-pink"
                    >
                      <Trash2 className="h-4 w-4" />
                    </Button>
                  )}
                </div>
              </CardHeader>
              <CardContent className="p-6">
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                                     {/* Input Section */}
                   <div className="space-y-4">
                     <div>
                       <label className="block text-sm font-medium text-files-headline-black mb-2">
                         Keyword *
                       </label>
                       <Input
                         placeholder="Enter your target keyword..."
                         value={row.keyword}
                         onChange={(e) => updateKeyword(row.id, e.target.value)}
                         className="w-full border-files-light-pink focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all"
                       />
                     </div>
                     
                     <div>
                       <label className="block text-sm font-medium text-files-headline-black mb-2">
                         Product
                       </label>
                       <Select
                         value={row.product}
                         onChange={(value) => updateProduct(row.id, value)}
                         options={productOptions}
                         placeholder="Select product..."
                         className="w-full"
                       />
                     </div>

                     <Button
                       onClick={() => generateContent(row.id)}
                       disabled={!row.keyword || row.isLoading}
                       className="w-full bg-gradient-to-r from-files-primary-red to-files-bright-red hover:from-files-maroon hover:to-files-primary-red text-white shadow-md hover:shadow-lg transition-all duration-200"
                     >
                      {row.isLoading ? (
                        <>
                          <Loader2 className="h-4 w-4 mr-2 animate-spin" />
                          Generating Content...
                        </>
                      ) : (
                        <>
                          <Wand2 className="h-4 w-4 mr-2" />
                          Generate Content
                        </>
                      )}
                    </Button>
                  </div>

                                     {/* Output Section */}
                   <div className="space-y-4">
                     <div>
                       <label className="block text-sm font-medium text-files-headline-black mb-2">
                         Article Title
                       </label>
                       <div className="relative">
                         <Textarea
                           placeholder="Article title will appear here..."
                           value={row.articleTitle}
                           readOnly
                           className="w-full h-20 resize-none text-sm pr-12 border-files-light-pink bg-files-light-gray/50"
                         />
                         {row.articleTitle && (
                           <div className="absolute top-2 right-2">
                             <CopyButton text={row.articleTitle} />
                           </div>
                         )}
                       </div>
                     </div>

                     <div>
                       <label className="block text-sm font-medium text-files-headline-black mb-2">
                         Meta Title
                       </label>
                       <div className="relative">
                         <Textarea
                           placeholder="Meta title will appear here..."
                           value={row.metaTitle}
                           readOnly
                           className="w-full h-16 resize-none text-sm pr-12 border-files-light-pink bg-files-light-gray/50"
                         />
                         {row.metaTitle && (
                           <div className="absolute top-2 right-2">
                             <CopyButton text={row.metaTitle} />
                           </div>
                         )}
                       </div>
                     </div>

                     <div>
                       <label className="block text-sm font-medium text-files-headline-black mb-2">
                         Meta Description
                       </label>
                       <div className="relative">
                         <div className="relative">
                           <Textarea
                             placeholder="Meta description will appear here..."
                             value={row.metaDescription}
                             readOnly
                             className="w-full h-20 resize-none text-sm pr-12 border-files-light-pink bg-files-light-gray/50"
                           />
                           {row.metaDescription && (
                             <div className="absolute top-2 right-2">
                               <CopyButton text={row.metaDescription} />
                             </div>
                           )}
                         </div>
                       </div>
                     </div>
                   </div>
                </div>

                                 {/* Full Article Section */}
                 {row.fullArticle && (
                   <div className="mt-6 pt-6 border-t border-files-light-pink">
                     <div className="flex items-center justify-between mb-4">
                       <label className="block text-sm font-medium text-files-headline-black">
                         Full Article
                       </label>
                       <div className="flex gap-2">
                         <button
                           onClick={() => openPreview(row.fullArticle, row.articleTitle)}
                           className="p-2 rounded-md bg-files-light-pink hover:bg-files-super-light-red text-files-primary-red transition-colors"
                           title="Preview Article"
                         >
                           <Eye className="h-4 w-4" />
                         </button>
                         <CopyButton text={row.fullArticle} />
                       </div>
                     </div>
                     <div className="relative">
                       <Textarea
                         placeholder="Full article will appear here..."
                         value={row.fullArticle}
                         readOnly
                         className="w-full h-48 resize-none text-sm border-files-light-pink bg-files-light-gray/50"
                       />
                     </div>
                   </div>
                 )}
              </CardContent>
            </Card>
          ))}
        </div>
      </div>

      {/* Article Preview Modal */}
      <Modal
        isOpen={previewModal.isOpen}
        onClose={closePreview}
        title={previewModal.title || 'Article Preview'}
        onCopy={copyPreviewContent}
      >
        <MarkdownPreview content={previewModal.content} />
      </Modal>
    </div>
  )
}

export default App 